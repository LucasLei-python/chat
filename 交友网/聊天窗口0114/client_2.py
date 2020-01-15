from socket import *
from threading import Thread

s=socket()

s.connect(('127.0.0.1',8888))
s.send(b"client_2,client_1")

def receive(s):
    while True:
        b = s.recv(1024)
        if b:
            print(b.decode())

def send(s):
    while True:
        a=input('please input:')
        if a:
            s.send(a.encode())

t1 = Thread(target=receive, args=(s,))
t1.start()

t2 = Thread(target=send, args=(s,))
t2.start()
