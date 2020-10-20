import asyncio


class EchoHandler:

    def __init__(self):
        self.msg = ''

    def __call__(self, *args, **kwargs):
        if len(args):
            self.msg = args[0]
        elif "msg" in kwargs.keys():
            self.msg = kwargs["msg"]
        else:
            self.msg = ''
        return self.msg


class ClientServerProtocol(asyncio.Protocol):

    def connection_made(self, transport):
        self._transport = transport
        self._handler = EchoHandler()

    def data_received(self, data):
        print("Received: ", data)
        resp = self._handler(data.decode())
        if resp == "close":
            self._transport
        self._transport.write(resp.encode())


class ConcurrentTcpServer:

    def __init__(self, ip, port, handler=EchoHandler()):
        assert type(ip) == str
        assert type(port) == int
        assert callable(handler)
        self._ip = ip
        self._port = port
        self._msg_handler = handler
        self._loop = asyncio.get_event_loop()
        self._coro = self._loop.create_server(
            ClientServerProtocol,
            self._ip, self._port
        )
        self._server = self._loop.run_until_complete(self._coro)

    def run(self):
        try:
            self._loop.run_forever()
        except KeyboardInterrupt:
            pass
        self._server.close()
        self._loop.run_until_complete(self._server.wait_closed())
        self._loop.close()


if __name__ == "__main__":
    server = ConcurrentTcpServer("127.0.0.1", 2222)
    server.run()
