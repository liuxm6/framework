# coding=utf-8
import tornado.web
import database

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.db = database.db 
    def on_finish(self):
        self.db.close()
class AppHandler(BaseHandler):
    _first_run = True
