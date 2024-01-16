
# Create your views here.
from django.shortcuts import render
import socket
def index(request):
    return render(request, 'index.html')

def socket_connect(request):
    s = socket.socket()
    port = 1026

    s.bind(('192.168.1.9', port))
    print("socket binded to", port)
    s.listen(5)

    while True:
        c, addr = s.accept()
        print("Connection established from ", addr)
        
        print("Running.....")
        
    s.close()
    return render(request, 'index.html')
        