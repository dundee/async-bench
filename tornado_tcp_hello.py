from tornado.tcpserver import TCPServer
from tornado.ioloop import IOLoop
from tornado.gen import coroutine
import tornado

class Handler(TCPServer):
    @coroutine
    def handle_stream(self, stream, address):
       try:
           yield stream.read_until(b"\r\n\r\n")
           yield stream.write('Hello world!')
           stream.close()
       except tornado.iostream.StreamClosedError:
            pass

server = Handler()
server.listen(9000)
IOLoop.current().start()
