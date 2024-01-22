#!/usr/bin/env python3
"""DB Module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session
    
    def add_user(self, email: str, hashed_password: str) -> User:
        """
        adds a new user to the database
        Args:
            email (str): email of user
            hashed_password (str): hashed pass of user
        Returns:
            User: created User object
        """
        # create a new user object
        new_user = User(email=email, hashed_password=hashed_password)
        # add new user to session and commit it to database
        self._session.add(new_user)        
        self._session.commit()

        # return new user object
        return new_user
    