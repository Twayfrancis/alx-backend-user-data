#!/usr/bin/env python3
"""Module for logging data with obfuscation of sensitive fields."""

import re
import logging
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields, redaction, message, separator):
    """
    Obfuscates specified fields in a log message.

    Args:
    fields (list): A list of strings representing the field names to obfuscate.
    redaction (str): A string representing the value to replace the field values with.
    message (str): A string representing the log message.
    separator (str): A string representing the character that separates fields in the log message.

    Returns:
    str: The log message with the specified fields obfuscated.
    """
    for field in fields:
        message = re.sub(f"{field}=[^;]*", f"{field}={redaction}", message)
    return message

class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        message = super().format(record)
        for field in self.fields:
            message = re.sub(f"{field}=[^;]*", f"{field}={self.REDACTION}", message)
        return message

def get_logger() -> logging.Logger:
    """
    Returns a logging.Logger object.

    The logger is named "user_data" and only logs up to logging.INFO level.
    It does not propagate messages to other loggers.
    It has a StreamHandler with RedactingFormatter as formatter.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    sh = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    sh.setFormatter(formatter)
    logger.addHandler(sh)
    return logger
