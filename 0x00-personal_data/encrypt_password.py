#!/usr/bin/env python3
"""Module for logging data with obfuscation of sensitive fields."""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Returns a salted, hashed password, which is a byte string.

    Args:
    password (str): The password to hash.

    Returns:
    bytes: The hashed password.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates that the provided password matches the hashed password.

    Args:
    hashed_password (bytes): The hashed password.
    password (str): The password to validate.

    Returns:
    bool: True if the password is valid, False otherwise.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
