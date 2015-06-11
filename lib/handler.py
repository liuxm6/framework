# coding=utf-8
import tornado.web
import database
import random

class BaseHandler(tornado.web.RequestHandler):
    _first_run = True
    def initialize(self):
        _first_run = False 
    #def finish(self, chunk=None):
    def on_finish(self):
        self.db.close()
    @property
    def masters(self):
        return self.application.masters
    @property
    def slaves(self):
        return self.application.slaves
    @property
    def db(self):
        return random.choice(self.application.sessions)
    @property
    def cache(self):
        return self.application.cache
    @property
    def cache_type(self):
        return self.application.cache_type
class AppHandler(BaseHandler):

    pass
