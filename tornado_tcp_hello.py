from tornado.tcpserver import TCPServer
from tornado.ioloop import IOLoop
from tornado.gen import coroutine

class Handler(TCPServer):
    @coroutine
    def handle_stream(self, stream, address):
       yield stream.read_until(b"\r\n\r\n")
       stream.write('Hello world!')
       stream.close()

server = Handler()
server.listen(9000)
IOLoop.current().start()
