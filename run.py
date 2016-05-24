#!/usr/bin/python

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

from tornado.options import define,options
import os,random

define('port',default=8080,type=int,help='server port')

class InfoHandler(tornado.web.RequestHandler):
    def get(self):
	    self.render('index.html',book='<<&abc>>')

class InfoPostHandler(tornado.web.RequestHandler):
    def post(self):
        name = self.get_argument('name')
        mail = self.get_argument('email')
        phone = self.get_argument('phone')
        addr = self.get_argument('address')
        self.render('info.html',name=name,mail=mail,phone=phone,address=addr)

    def write_error(self, status_code, **kwargs):
        self.write('why? status code: %d' % status_code)

class MungerHandler(tornado.web.RequestHandler):
    def map_by_first_letter(self,text):
        mapped = dict()
        for line in text.split('\r\n'):
            for word in [x for x in line.split(' ') if len(x) > 0 ]:
                if word[0] not in mapped:
                    mapped[word[0]] = []
                    mapped[word[0]].append(word)
        return mapped

    def get(self):
        self.render('munger.html')

    def post(self):
        source_text = self.get_argument('source')
        text_to_chage = self.get_argument('change')
        source_map = self.map_by_first_letter(source_text)
        change_lines = text_to_chage.split('\r\n')
        # self.write('source_text: %s, %s ' % (source_text,text_to_chage))
        self.render('munged.html',source_map=source_map,change_lines=change_lines,choice=random.choice)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("It's OK!")
    def post(self):
        name = self.get_argument('name')
        self.write('Post Content: %s' % str(name))
    def write_error(self, status_code, **kwargs):
        self.write('Error Code: %d' % status_code)

def make_app():
    return tornado.web.Application(handlers=[
    (r'/info',InfoHandler),
    (r'/infopst',InfoPostHandler),
    (r'/munger',MungerHandler),
    (r'/',IndexHandler)],
    template_path=os.path.join(os.path.dirname(__file__),"templates"),
    static_path=os.path.join(os.path.dirname(__file__),"static"),
    )

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
