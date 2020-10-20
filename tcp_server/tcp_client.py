import socket


class TestTcpClient:

    def __init__(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self, addr, msgs):
        self._socket.connect(addr)
        for m in msgs:
            self._socket.send(m.encode())
        self._socket.close()


if __name__ == "__main__":
    server = TestTcpClient()
    server.run(("127.0.0.1", 2222), ["Test", "message", "set"])