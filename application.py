#!/usr/bin/python

import os
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

import handler.index

from tornado.options import define,options

define('port',default=8081,type=int,help='server port')

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
                (r'/',handler.index.IndexHandler),
                (r'/post',handler.index.PostPageHandler),
        ]

        settings = dict(
                template_path=os.path.join(os.path.dirname(__file__),"templates"),
        )

        tornado.web.Application.__init__(self,handlers,**settings)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
