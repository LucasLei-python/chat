from flask import Flask
from flask import render_template
from flask import request
import json
from socket import *
from threading import Thread
from time import sleep

app =  Flask(__name__,)


@app.route('/chat3')
def reg_view2():
    return render_template('chat3.html')

@app.route('/client')
def client_01():
    sender = request.args.get('sender')
    receiver = request.args.get('receiver')
    con_info="%s,%s" %(sender,receiver)
    s=socket()
    s.connect(('127.0.0.1',8888))
    s.send(con_info.encode())
    content = request.args.get('content')
    list_1=[]
    def receive(s):
        while True:
            b = (s.recv(1024)).decode()
            if b=='done':
                break
            else:
                list_1.append(b)
                print(b)
                print(list_1)


    def send(s):
        if content:
            print(content)
            sleep(0.1)
            s.send(content.encode())

    t2 = Thread(target=send, args=(s,))
    t2.start()
    t1 = Thread(target=receive, args=(s,))
    t1.start()
    t1.join()
    t2.join()
    s.close()
    print(list_1)
    list2=[str(i) for i in list_1]
    s=' '.join(list2)
    print(s)
    return s


if __name__ == '__main__':
    app.run(debug=False)
