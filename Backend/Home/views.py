
# Create your views here.
from django.shortcuts import render
import socket
def index(request):
    return render(request, 'index.html')

import threading
import socket

def socket_connect(request):
    s = socket.socket()
    port = 1026

    s.bind(('192.168.1.9', port))
    print("socket binded to", port)
    s.listen(5)

    def run():
        while True:
            c, addr = s.accept()
            print("Connection established from ", addr)
            data = c.recv(1024).decode()
            if not data or data == "Break":
                print("ending the connection")
                break
            print("Running.....", data)

        s.close()

    thread = threading.Thread(target=run)
    thread.start()

    return render(request, 'index.html')
    