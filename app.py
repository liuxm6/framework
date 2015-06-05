from tornado.options import options
from lib.database import db
from lib.cache import cache
from lib.locale import locale
from urls import handlers

import tornado.httpserver
import tornado.ioloop
import config

class Application(tornado.web.Application):
    def __init__(self):
        #app
        tornado.web.Application.__init__(self,handlers,**config.settings)
        #db
        db.init_db()
        #cache
        cache.init_cache();
        #locale
        locale.init_locale();
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
if __name__ == "__main__":
    main()
