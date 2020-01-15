import pymysql
from socket import *
from threading import Thread
import sys
import datetime
from DBUtils.PooledDB import PooledDB



def mysql_connection():
    maxconnections = 20
    pool = PooledDB(
        pymysql,
        maxconnections,
        host='176.140.10.103',
        user='exchange',
        port=3306,
        passwd='321',
        db='soul',
        charset='utf8',
        use_unicode=True)
    return pool


HOST = '0.0.0.0'

PORT = 8888
ADDR = (HOST, PORT)


# 处理客户端请求
def handle(c):
    data = c.recv(1024)
    print(data.decode())
    list = str(data.decode()).split(',', 2)
    for i in list:
        print(i)
    print(list)
    sender = list[0]
    receiver = list[1]
    time_now = datetime.datetime.now()
    n = ''

    def send(c):
        sql1 = "select * from chat where status=%s and receiver=%s;"
        sql3 = "update chat set status='sent' where sender=%s and time=%s;"
        while True:
            pool = mysql_connection()
            con = pool.connection()
            cur = con.cursor()
            cur.execute(sql1, (n, sender))
            list01 = cur.fetchall()
            if len(list01):
                for i in list01:
                    c.send(("%s:%s:%s" % (i[0], i[2], i[3])).encode())
                    cur.execute(sql3, (i[0], i[3]))
                    con.commit()
                c.send(b'done')
            cur.close()
            con.close()

    def receive(c):
        while True:
            pool = mysql_connection()
            con = pool.connection()
            cur = con.cursor()
            content = (c.recv(1024)).decode()
            if content:
                sql2 = "insert into chat values(%s,%s,%s,%s,%s);"
                cur.execute(sql2, (sender, receiver, content, time_now, n))
                con.commit()
            cur.close()
            con.close()

    t1 = Thread(target=send, args=(c,))
    t1.setDaemon(True)
    t1.start()
    t2 = Thread(target=receive, args=(c,))
    t2.setDaemon(True)
    t2.start()


# 创建tcp套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(3)

print("Listen the port 8888...")
# 循环接收客户端链接
while True:
    try:
        c, addr = s.accept()
        print("Connect from", addr)
    except KeyboardInterrupt:
        sys.exit('服务器退出')
    except Exception as e:
        print(e)
        continue

    #  创建线程处理
    t = Thread(target=handle, args=(c,))
    t.setDaemon(True)  # 主线程退出其他线程也退出
    t.start()