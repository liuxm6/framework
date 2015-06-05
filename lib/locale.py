import tornado.httpserver
from tornado.options import define, options
class locale(object):

    """Docstring for . """

    def __init__(self):
        """TODO: to be defined1. """
    def init_locale(self):
        """TODO: Docstring for init_locale.
        :returns: TODO

        """
        tornado.locale.load_translations(options.site_locale_path)
        tornado.locale.set_default_locale(options.site_default_locale)
locale = locale()
