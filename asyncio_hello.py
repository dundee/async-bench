# https://github.com/oberstet/scratchbox/blob/master/python/asyncio/tcp_echo_server.py

try:
   import asyncio
except ImportError:
   import trollius as asyncio

import sys

try:
   import signal
except ImportError:
   signal = None

import psutil
p = psutil.Process()
print (p.cpu_affinity())
p.cpu_affinity([0])
print (p.cpu_affinity())

class EchoServer(asyncio.Protocol):

   def connection_made(self, transport):
      self.transport = transport

   def data_received(self, data):
      if data in (b'\r\n', b'\n') or b'\r\n\r\n' in data:
          self.transport.write(b'HTTP/1.1 200 OK\n\n')
          self.transport.write(b'Hello world!')
          self.transport.close()


loop = asyncio.get_event_loop()
print ('Using backend: {0}'.format(loop.__class__.__name__))

loop.add_signal_handler(signal.SIGINT, loop.stop)

f = loop.create_server(EchoServer, port = 9000, backlog = 1024)
server = loop.run_until_complete(f)
try:
   print ('Listening on port 9000')
   loop.run_forever()
finally:
   server.close()
   loop.close()
