import tornado.httpserver
import tornado.ioloop

def handle_request(request):
  request.write("HTTP/1.1 200 OK\r\n\r\nHello world!")
  request.finish()

http_server = tornado.httpserver.HTTPServer(handle_request)
http_server.listen(9000)
tornado.ioloop.IOLoop.instance().start()
