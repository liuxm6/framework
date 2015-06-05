from tornado.web import url
from lib.handler import AppHandler
from model import *

class IndexHandler(AppHandler):
    def get(self):
        self.db.session.query(User)
        self.render('index.html')

handlers = [
    url(r"/",IndexHandler,name="index"),
]
