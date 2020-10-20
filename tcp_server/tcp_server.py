import socket


class EchoTcpServer:

    def __init__(self, ip, port):
        self._ip = ip
        self._port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind((self._ip, self._port))
        self._socket.listen(1)

    def run(self):
        conn, addr = self._socket.accept()
        while True:
            data = conn.recv(1024)
            print("Received: ", data)
            if not data or data == "close":
                break
            conn.send(data)
        conn.close()


if __name__ == "__main__":
    server = EchoTcpServer("127.0.0.1", 2222)
    server.run()
