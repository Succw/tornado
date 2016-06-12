#!/usr/bin/python

import os
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

import handler.index
import handler.dns

from tornado.options import define,options

define('port',default=8081,type=int,help='server port')

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/dns', handler.dns.IndexHandler)
        ]

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__),"templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
        )

        tornado.web.Application.__init__(self,handlers,**settings)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()