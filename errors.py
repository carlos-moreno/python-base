#!/usr/bin/env python

import os
import sys
import time
import logging

log = logging.Logger("errors")

# EAFP - Easy to Ask Forgiveness than permission
#      - Giria para dizer algo como `É mais fácil pedir perdão do que permissão`


def try_to_open_a_file(filepath, retry=0):
    """Tries to open a file, if error, retries n times."""
    if retry > 999:
        raise ValueError("Retry cannot be above 999")
    try:
        return open(filepath).readlines()
    except FileNotFoundError as e:
        log.error("ERROR: %s", e)
        time.sleep(2)
        if retry > 1:
            return try_to_open_a_file(filepath, retry=retry - 1)
    else:
        print("SUcesso!!!")
    finally:
        print("Execute isso sempre")

    return []


for line in try_to_open_a_file("names.txt", retry=5):
    print(line)
