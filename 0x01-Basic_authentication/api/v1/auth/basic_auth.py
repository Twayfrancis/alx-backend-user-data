#!/usr/bin/env python3
''' basic authentication file'''
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth that inherits from Auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Method that extracts the Base64 Authorization header """
        if authorization_header is None or type(
                                authorization_header) is not str:
            return None

        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header.split(' ')[1]
