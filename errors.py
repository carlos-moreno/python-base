#!/usr/bin/env python

import os
import sys

# LBYL - Look Before You Leap
#      - Giria para dizer algo como `OLhe antes de pular`

if os.path.exists("names.txt"):
    print("The file exists.")
    input("...")  # Race Condition
    names = open("names.txt").readlines()
else:
    print("[Error] File names.txt not found.")
    sys.exit(1)

if len(names) >= 4:
    print(names[3])
else:
    print("[Error] Missing name in the list.")
    sys.exit(1)
