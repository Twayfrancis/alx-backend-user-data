#!/usr/bin/env python3
"""DB Module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

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
        if not email or not hashed_password:
            return
        user = User(email=email, hashed_password=hashed_password)
        # add new user to session and commit it to database
        session = self._session
        self._session.add(user)
        self._session.commit()

        # return new user object
        return user

    def find_user_by(self, **kwargs) -> User:
        """
        finds user in database by keyword args
        args:
            **kwargs: arbitary keyword args.
        Returns:
            User: first user object that matches keyword
        Raises:
            sqlalchemy.orm.exc.NoResultFound: if user not found
            sqlalchemy.exc.InvalidRequestError: If wrong query args passed
        """
        try:
            return self._session.query(User).filter_by(**kwargs).first()
        except NoResultFound:
            raise
        except InvalidRequestError:
            raise
