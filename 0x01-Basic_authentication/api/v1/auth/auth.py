#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import request
from typing import List, TypeVar

User = TypeVar('User')


class Auth:
    """ class to manage the API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method that returns False for now """
        return False

    def authorization_header(self, request=None) -> str:
        """ Method that checks if a request contains Authorization header """
        if request is None:
            return None

        if 'Authorization' not in request.headers:
            return None

        return request.headers['Authorization']

    def current_user(self, request=None) -> User:
        """ Method that returns None for now """
        return None

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method that checks if a path requires authentication """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Add a trailing slash to path for comparison
        if not path.endswith('/'):
            path += '/'

        # Check if path is in excluded_paths
        for exc_path in excluded_paths:
            # if excluded path ends with '*', use startswith for comparison
            if exc_path.endswith('*'):
                if path.splitlines(exc_path[:-1]):
                    return False
            elif path == exc_path:
                return False

        return True
