import datetime, socket ,threading ,csv ,time ,json
from rest_framework import generics
from django.shortcuts import render
from .models import DeviceUser
from .serializers import DeviceUserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


def index(request):
    conn = check_active_conections()
    all_users = DeviceUser.objects.all()
    context = {'active': len(conn), 'list': conn, 'total_users':all_users}
    json_data = json.dumps(context)
    return render(request, 'index.html', {'json_data': json_data})

active = 0
port = 4444
is_running = True
t_id = 1000
s = socket.socket()
active_list = []
        
@api_view(['GET'])
def socket_bind(*args, **kwargs):
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(('192.168.1.9', port))
    print("socket binded successfuly on port:", port)
    return Response({'message': 'Socket Binded successfuly'})






@api_view(['GET'])
def socket_connect(request):
    global is_running
    global t_id
    
    print("socket listening to", port)
    data = {'status': 'socket connected'}
    s.listen(5)

    def run():
        global is_running
        global active
        try:
            start_time = time.time()
            filename = 'sensordata_' + str(int(start_time / 5)) + '.csv'
            f = open(filename, 'w', newline='')
            # Create a CSV writer object
            writer = csv.writer(f)
            writer.writerow(['Acc(x)', 'Acc(y)', 'Acc(z)', 'Gyr(x)', 'Gyr(y)', 'Gyr(z)', 'Mag(x)', 'Mag(y)', 'Mag(z)'])
            print("csv writer is intialized")
            while True:
                    c, addr = s.accept()
                    print("Connection established from ", addr, "at:", datetime.datetime.now())    
                    id = c.recv(10).decode()
                    update_status(id)
                    active_list.append(id)
                    while is_running:
                        data = c.recv(1024).decode()
                        print(data)
                        if data == "":
                            print("finished................")
                            active_list.remove(id)
                            
                            break
                        
                        columns = data.split(',')
                        print(columns)
                        writer.writerow(columns)
                        elapsed_time = time.time() - start_time
                        if elapsed_time >= 50:
                            f.close()
                            start_time = time.time()
                            filename = 'sensordata_' + str(int(start_time / 5)) + '.csv'
                            f = open(filename, 'w', newline='')
                            writer = csv.writer(f)
                            writer.writerow(['Acc(x)', 'Acc(y)', 'Acc(z)', 'Gyr(x)', 'Gyr(y)', 'Gyr(z)', 'Mag(x)', 'Mag(y)', 'Mag(z)'])
                    
                    remove_status(id)
                    break

            f.close()
            c.close()
        except Exception:
            pass

        
        


    thread = threading.Thread(target=run)
    t_id = threading.get_ident()
    thread.start()

    return Response({'server_message': 'Server Opened successfuly'})
    
@api_view(['GET'])
def disconnect(request):
    global is_running
    global s
    print("connection has been closed")
    is_running = False
    s.close()
    s = socket.socket()
    return Response({'message': 'Socket disconnected successfuly'})

def check_active_conections():
    global active_list
    return active_list

class DeviceUserList(generics.ListAPIView):
    queryset = DeviceUser.objects.all()
    serializer_class = DeviceUserSerializer

def update_status(id):
    user = DeviceUser.objects.get(pk = id)
    user.status = "active"
    user.last_connected= datetime.datetime.now()
    user.save()

def remove_status(id):
    user = DeviceUser.objects.get(pk = id)
    user.status = "inactive"
    user.save()

@api_view
def get_active_users():
    users = DeviceUser.objects.filter(status = "active")
    return Response({'active': len(users)})

@api_view
def get_all_users():
    users = DeviceUser.objects.all()
    return Response({'active': len(users)})
