from tornado.web import url
from lib.handler import AppHandler
from model import *

class IndexHandler(AppHandler):
    def get(self):
        user = self.db.query(User).order_by(User.uid).first()
        self.cache.set('name',user.name)
        name = self.cache.get('name')
        self.render('index.html',name=name)

handlers = [
    url(r"/",IndexHandler,name="index"),
]
