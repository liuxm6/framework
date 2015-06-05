from lib.database import db
from datetime import datetime
from sqlalchemy import Column, Integer,String, ForeignKey, Table, Float, DateTime,Text
from sqlalchemy.orm import backref, mapper, relationship

class User(db.base):

    """Docstring for MyClass. """

    __tablename__ = 'sys_users'
    uid = Column(Integer,primary_key=True)
    name = Column(String(30),nullable=False)
    email = Column(String(50),nullable=False)
    password = Column(String(50),nullable=False)
    status = Column(Integer,nullable=False,default=0)
    create_time = Column(DateTime,nullable=False,default=datetime.now())
    update_time = Column(DateTime,nullable=False)
    roles = relationship("User_Role",backref='sys_users',order_by="User_Role.uid")

class Role(db.base):

    """Docstring for MyClass. """

    __tablename__ = 'sys_roles'
    rid = Column(Integer,primary_key=True)
    name = Column(String(50),nullable=False)
    users = relationship("User_Role",backref='sys_roles',order_by="User_Role.rid")

class User_Role(db.base):

    """Docstring for MyClass. """

    __tablename__ = 'sys_user_roles'
    id = Column(Integer,primary_key=True)
    uid = Column(Integer,ForeignKey('sys_users.uid')) 
    rid = Column(Integer,ForeignKey('sys_roles.rid')) 
