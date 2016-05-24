#!/usr/bin/python

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

from tornado.options import define,options
import os

define('port',default=8081,type=int,help='server port')

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
	    self.render('index.html')

class PostPageHandler(tornado.web.RequestHandler):
    def post(self):
        name = self.get_argument('name')
        mail = self.get_argument('email')
        phone = self.get_argument('phone')
        addr = self.get_argument('address')
        self.render('info.html',name=name,mail=mail,phone=phone,address=addr)

    def write_error(self, status_code, **kwargs):
        self.write('why? status code: %d' % status_code)

def make_app():
    return tornado.web.Application(handlers=[
	(r'/',IndexHandler),
    (r'/post',PostPageHandler)],
    template_path=os.path.join(os.path.dirname(__file__),"templates")
    )

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
