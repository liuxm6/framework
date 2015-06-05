import os
from tornado.options import define,options
rootdir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
# Version
define('version', 1.0)
# Site
define('title', type=str, default='Test')
define('url', type=str, default='http://www.test.com')
define('description', type=str, default='Decsription')
define('login_url', type=str, default='/login')
define('static_path', type=str, default=os.path.join(rootdir, 'static'))
define('template_path', type=str, default=os.path.join(rootdir, 'templates'))
define('locale_path', type=str, default=os.path.join(rootdir, 'locale'))
define('default_locale', type=str, default='zh_CN')
define('xsrf_cookies', type=bool, default=True)
define('cookie_secret', type=str,default='QkiIjc2rT+GlhhTBaBAQNLybcuOIj0j8lKN/LW8rrHA=')
# Timezone
define('timezone', type=str, default='Asia/Shanghai')
# Server
define('port', type=int, default=8002)
define('debug', type=bool, default=True)
# DataBase
define('master', type=str,default='mysql://demo:demo@localhost:3306/demo_blog?charset=utf8')
define('slaves', type=list, default=[])
# Cache
define('cache', type=str, default='memcache')
define('memcache', type=str, default='127.0.0.1:11211')
define('redis_host', type=str, default='')
define('redis_port', type=int, default=6379)
define('redis_db', type=int, default=0)
define('redis_password', type=str, default='')
define('redis_socket_timeout', type=int, default=None)
# File
# Theme
define('theme_name', type=str, default='default')
define('page', type=int, default=10)
# Mail
define('mail_notify', type=bool, default=False)
define('mail_host', type=str, default='smtp.gmail.com:587')
define('mail_username', type=str, default='')
define('mail_password', type=str, default='')
define('mail_from_addr', type=str, default='')