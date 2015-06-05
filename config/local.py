import os
from tornado.options import define,options

rootdir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

# Version
define('version', 1.0)
# Site
define('site_title', type=str, default='Test')
define('site_url', type=str, default='http://www.test.com')
define('site_description', type=str, default='Decsription')
define('site_login_url', type=str, default='/login')
define('site_static_path', type=str, default=os.path.join(rootdir, 'static'))
define('site_template_path', type=str, default=os.path.join(rootdir, 'template'))
define('site_locale_path', type=str, default=os.path.join(rootdir, 'translations'))
define('site_default_locale', type=str, default='zh_CN')
define('site_xsrf_cookies', type=bool, default=True)
define('site_cookie_secret', type=str,default='QkiIjc2rT+GlhhTBaBAQNLybcuOIj0j8lKN/LW8rrHA=')
# Timezone
define('timezone', type=str, default='Asia/Shanghai')
# Server
define('port', type=int, default=8002)
define('debug', type=bool, default=True)
# DataBase
define('master', type=str,default='mysql+mysqldb://root:@127.0.0.1/python_demo?charset=utf8')
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
