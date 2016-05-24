#!/usr/bin/python

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

from tornado.options import define,options

define('port',default=8081,type=int,help='server port')

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
	self.write('succw.com')

def make_app():
    return tornado.web.Application(handlers=[
	(r'/',IndexHandler),
])

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
