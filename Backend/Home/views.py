
import datetime 
import socket
import threading
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


s = socket.socket()
port = 4444
is_running = True

def socket_connect(request):
    global is_running
    
    s.bind(('192.168.1.9', port))
    print("socket binded to", port)
    s.listen(5)

    def run():
        global is_running
        
        while is_running:
            c, addr = s.accept()
            print("Connection established from ", addr, "at:", datetime.datetime.now())
            data = c.recv(1024).decode()
            if not data or data == "Break":
                print("ending the connection")
                break
            print(data)

        
        s.close()

    thread = threading.Thread(target=run)
    thread.start()

    return render(request, 'index.html')
    

def disconnect(request):
    global is_running
    
    print("connection has been closed")
    is_running = False

    return render(request, "index.html")
