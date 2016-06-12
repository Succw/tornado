#!/usr/bin/env python
#coding=utf-8

import os
import re
import fileinput
import datetime

import tornado.web

import conf.dns

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        domain = self.get_argument('domain')
        with open(conf.dns.settings['dnsmasq']) as hosts:
            if (domain):
                for hostname in hosts.readlines():
                    regx = re.search(domain,hostname)
                    if regx:
                        c=hostname.split()
                        self.write(c[1])
            else:
                for hostname in hosts.readlines():
                    c = hostname.split()
                    self.write(c[1])