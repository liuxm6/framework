from tornado.options import define, options
import local

settings = dict(
    debug = options.debug,
    site_title = options.site_title,
    xsrf_cookies = options.site_xsrf_cookies,
    cookie_secret = options.site_cookie_secret,
    template_path = options.site_template_path,
    static_path = options.site_static_path,
    login_url = options.site_login_url,
)