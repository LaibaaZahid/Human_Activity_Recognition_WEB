import datetime 
import socket
import threading
import concurrent.futures
from django.shortcuts import render
import csv
import time
from django.http import JsonResponse


def index(request):
    conn = check_active_conections()
    return render(request, 'index.html', {'active': len(conn), 'list': conn})

active = 0
port = 4444
is_running = True
t_id = 1000
s = socket.socket()
active_list = []
        
def socket_bind(request):
    global s
    s.bind(('192.168.100.46', port))
    print("socket binded successfuly on port:", port)
    data= {'status': 'success'}
    return JsonResponse(data)

""" seerat  making changes """


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
                if isinstance(s, socket.socket):
                    print("socket is available")
                    c, addr = s.accept()
                    print("Connection established from ", addr, "at:", datetime.datetime.now())    
                    id = c.recv(10).decode()
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
                    
                    break

            f.close()
            c.close()
        except Exception:
            pass

        
        


    thread = threading.Thread(target=run)
    t_id = threading.get_ident()
    thread.start()

    return JsonResponse(data)
    

def disconnect(request):
    global is_running
    global s
    print("connection has been closed")
    #is_running = False
    s.close()
    s = socket.socket()
    return render(request, "index.html")

def check_active_conections():
    global active_list
    return active_list