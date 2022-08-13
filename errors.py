#!/usr/bin/env python

import os
import sys

# EAFP - Easy to Ask Forgiveness than permission
#      - Giria para dizer algo como `É mais fácil pedir perdão do que permissão`

try:
    names = open("names.txt").readlines()
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit(1)
    # TODO: Usar retry
else:
    print("SUcesso!!!")
finally:
    print("Execute isso sempre")

try:
    print(names[3])
except:
    print("[Error] Missing name in the list.")
    sys.exit(1)
