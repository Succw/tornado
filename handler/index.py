#!/usr/bin/env python
#coding=utf-8

import tornado.web

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

