#!/usr/bin/env python3
"""function called filter_datum that returns the log message obfuscated"""

import re


def filter_datum(fields, redaction, message, separator):
    """
    Obfuscates specified fields in a log message.

    Args:
    fields (list): A list of strings representing the field names to obfuscate.
    redaction (str): A str repr value to replace the field values with.
    message (str): A str repr  log message.
    separator (str): A str repr char that separates fields in the log message.

    Returns:
    str: The log message with the specified fields obfuscated.
    """
    for field in fields:
        message = re.sub(f"{field}=[^;]*", f"{field}={redaction}", message)
    return message
