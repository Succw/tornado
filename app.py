#!/usr/bin/python

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import os


from tornado.options import define,options

define('port',default=8081,type=int,help='server port')

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("echo")

class PostPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Post")

# class Application(tornado.web.Application):
#     def __init__(self):
#         handlers = [
#             (r'/',IndexHandler),
#             (r'/post',PostPageHandler),
#         ]
#
#         settings = dict(
#             template_path = os.path.join(os.path.dirname(__file__),"templates")
#         )

# class Application(tornado.web.Application):
#     def __init__(self):
#         handlers = [
#                 (r'/',IndexHandler),
#                 (r'/post',PostPageHandler),
#         ]
#
#         settings = dict(
#                 template_path=os.path.join(os.path.dirname(__file__),"templates"),
#                 Debug=True,
#         )
#
#         tornado.web.Application.__init__(self,handlers,**settings)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/',handler.index.IndexHandler),
            (r'/post',handler.index.PostPageHandler)
        ]

        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__),"templates")
        )
        tornado.web.Application.__init__(self,)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()