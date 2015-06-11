#!/usr/bin/env python
# encoding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from tornado.options import options

import random
import config

class InitDB(object):
    def __init__(self,**kwargs):
        self.engines = []
        self.sessions = []
        self.masters = []
        self.slaves = []
        for master in options.masters:
            master = create_engine(
                master,
                echo=options.debug,
                convert_unicode=True,
                pool_recycle=3600
            )
            self.engines.append(master)
            self.masters.append(
                scoped_session(sessionmaker(bind=master))
            )
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
        self.sessions = self.masters + self.slaves
    @property
    def engine(self):
        return random.choice(self.engines)
    @property
    def session(self):
        return random.choice(self.sessions)
    @property
    def base(self):
        if hasattr(self, '_base'):
            _base = self._base
        else:
            _base = declarative_base()
            self._base = _base
        if self.slaves:
            slave = random.choice(self.slaves)
            _base.query = slave.query_property()
        else:
            master = random.choice(self.masters)
            _base.query = master.query_property()
        return _base 
    def init_db(self):
        self.base.metadata.create_all(bind=self.engine)
    def drop_db(self):
        self.base.metadata.drop_all(self.engine)
db = InitDB()
