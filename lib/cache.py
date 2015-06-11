from tornado.options import options

import config

class cache(object):

    def __init__(self):
        self.cache_type = options.cache
    @property
    def cache(self):
        return  {
                'memcache':lambda:self.memcache(),
                'redis':lambda:self.redis(),
                'None':lambda:None
                }[self.cache_type]()
    def memcache(self):
        from pymemcache.client import Client
        cache = Client((
            options.memcache_host,
            options.memcache_port))
        return cache 
    def redis(self):
        import redis
        cache = redis.Redis(
                host=options.redis_host,
                port=options.redis_port,
                db=options.redis_db,
                password=options.redis_password,
                socket_timeout=options.redis_socket_timeout)
        return cache
    def init_cache(self):
        """TODO: Docstring for init_cache.
        :returns: TODO

        """
        pass
cache = cache();
