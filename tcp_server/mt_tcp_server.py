import threading
import socket


def handler(conn):
    while True:
        data = conn.recv(1024)
        if data and data != "close":
            conn.send(data)
        else:
            break
    conn.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 2222))
s.listen(10)

thread_pool = []

while True:
    conn, addr = s.accept()
    t = threading.Thread(target=handler, args=(conn,))
    t.run()
    thread_pool.append(t)
