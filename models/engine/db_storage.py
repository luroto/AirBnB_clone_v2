#!/usr/bin/python3
""" This file manage all the database """

import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from models import BaseModel, Base


class DBStorage:
    """ this class will contain all the manages of database
    """

    __engine = None
    __session = None

    def __init__(self):
        """ this contain the definition of environ variables
            the creation of engine and the reload that if
            the test is equal to the environment should drop
            down all the tables.
        """

        envi = os.environ('HBNB_ENV')
        my_user = os.environ('HBNB_MYSQL_USER')
        my_psswd = os.environ('HBNB_MYSQL_PWD')
        my_host = os.environ('HBNB_MYSQL_HOST')
        my_datab = os.environ('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(my_user, my_psswd,
                                              my_host, my_datab))
        self.reload()
        if 'test' == envi:
            Base.metadata.drop_all(tables)

    def all():
        """ this contain the filter that depend of the class
            that is specified
        """
        dicti = {}
        list_cls = []

        if cls is None:
            list_cls += State.query(cls).all()
            list_cls += City.query(cls).all()
            list_cls += User.query(cls).all()
            list_cls += Amenity.query(cls).all()
            list_cls += Place.query(cls).all()
            list_cls += Review.query(cls).all()

        else:
            self.__session.query(cls).all()

        for var in list_cls:
            k = type(var).__name__ + '.' + var.id
            dicti[k] = var

        return dicti

    def new(self, obj):
        """ add the object to session """

        self.__session.add(obj)

    def save(self):
        """ commit all the changes to session """

        self.__session.commit(obj)

    def delete(self, obj=None):
        """ delete from the session """

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ This function create all the tables and the session """

        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine),
                                        expire_on_commit=False)
