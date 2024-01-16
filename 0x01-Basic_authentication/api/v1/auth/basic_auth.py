#!/usr/bin/env python3
''' basic authentication file'''
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """method that decodes a base64 authrorization header"""
        if base64_authorization_header is None or type(
                base64_authorization_header) is not str:
            return None

        try:
            base64_bytes = base64_authorization_header.encode('utf-8')
            message_bytes = base64_b64decode(base64_bytes)
            return message_bytes.decode('utf-8')
        except Exception:
            return None
