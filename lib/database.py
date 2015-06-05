from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from tornado.options import options

import random
import config

class InitDB(object):

    """Docstring for MyClass. """

    def __init__(self,**kwargs):
        """TODO: to be defined1. """
        self.engine = create_engine(
            options.master,
            echo=options.debug,
            convert_unicode=True,
            pool_recycle=3600
        )
        self.session = scoped_session(
            sessionmaker(bind=self.engine)
        )
        self.slaves = []
        for slave in options.slaves:
            slave = create_engine(
                slave,
                echo=options.debug,
                convert_unicode=True,
                pool_recycle=3600
            )
            self.slaves.append(
                scoped_session(sessionmaker(bind=slave))
            )
    @property
    def base(self):
        """TODO: Docstring for function.

        :arg1: TODO
        :returns: TODO

        """
        if hasattr(self, '_base'):
            _base = self._base
        else:
            _base = declarative_base()
            self._base = _base
        if self.slaves:
            slave = random.choice(self.slaves)
            _base.query = slave.query_property()
        else:
            _base.query = self.session.query_property()
        return _base 
    def init_db(self):
        """TODO: Docstring for function.

        :arg1: TODO
        :returns: TODO

        """
        self.base.metadata.create_all(bind=self.engine)
    def drop_db(self):
        """TODO: Docstring for function.

        :arg1: TODO
        :returns: TODO

        """
        self.base.metadata.drop_all(self.engine)
    def query(self,**kwargs):
        """TODO: Docstring for query.

        :g1: TODO
        :returns: TODO

        """
        return self.base.query(); 
    def close(self):
        """TODO: Docstring for function.

        :arg1: TODO
        :returns: TODO

        """
        self.session.close();
db = InitDB()
