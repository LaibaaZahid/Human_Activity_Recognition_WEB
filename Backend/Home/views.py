import socket ,threading ,csv ,time ,json
from rest_framework import generics
from django.shortcuts import render
from .models import DeviceUser
from .serializers import DeviceUserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime

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
sensors = ["Accelerometer", "Gyroscope", "Magnetometer", "Proximity", "LinearAcceleration", "StepCounter", "Gravity", "RotationVector"]
        
@api_view(['GET'])
def socket_bind(*args, **kwargs):
    global s
    s.bind(('192.168.1.8', port))
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
            while True:
                    # Establishing connection ############
                    c, addr = s.accept()
                    print("Connection established from ", addr, "at:", datetime.now())    
                    
                    # Receiving user id ##########
                    id = c.recv(10).decode()
                    print("User ID received : ", id)

                    # Getting active sensors list #########
                    data = c.recv(22).decode() # Assuming socket_stream is a socket object
                    numbers = data.split(',')  # Split the string by commas to get individual numbers
                    print(numbers)
                    indexes_of_1 = [i for i, num in enumerate(numbers) if num == ' 1' or num == '1']  # Get indexes where 1 is present
                    filenames = [f"{sensors[i]}.csv" for i in indexes_of_1]
                    print("indexes of 1:", indexes_of_1)
                    print("selected sensors: ",filenames)
                    ##################### Sensor list generated now ##################################
                    
                    bytes_to_read_per_line = len(indexes_of_1)*25

                    #################### csv writers initialized #####################################
                    csv_writers = {}
                    for filename in filenames:
                        csv_file = open(filename, 'a', newline='')
                        csv_writers[filename] = csv.writer(csv_file)
                    #################### writers for selected sensors selected #########################

                    buffer = ''
                    i = 0
                            
                    while is_running:
                        data = c.recv(1).decode()
                        #print(data, "--------------------------")
                        if data == "" or not data:
                            print("finished................")
                            #active_list.remove(id)
                            break
                        
                        
                        if data == "$":

                            buffer = buffer.strip()
                            print("buffer = ", buffer)
                            sensor_data = buffer.split(',')
                            sensor_data.append(id)
                            sensor_data.append(datetime.now())
                            buffer= ''
                            # Split the data into chunks corresponding to the indexes
                            #chunks = [sensor_data[i:i+3] for i in range(0, len(sensor_data), 3)]
                            print(sensor_data, " to be writing to ----------", sensor_data[0])
                            #for i, chunk in enumerate(chunks):
                            filename = sensor_data[0]
                            print(csv_writers)
                            csv_writers[filename].writerow(sensor_data[1:])
                            print("data written")
                            i += 1
                            if i >= len(indexes_of_1):
                                i = 0
                        else:
                            buffer += data

                    #remove_status(id)
                    break

            
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
