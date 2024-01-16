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
        """ Method that returns None for now """
        return None

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
        if path in excluded_paths:
            return False

        return True
