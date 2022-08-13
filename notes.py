#!/usr/bin/env python
"""Bloco de notas

$ notes.py new "Titulo"
tag: tech
text: informe o texto da nota

$ notes.py read tech
"""
__version__ = "0.1.0"
__author__ = "Carlos Moreno"

import os
import sys

cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage.")
    print(f"You must specify subcommand {cmds}")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")

if arguments[0] == "read":
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"Title: {title}")
            print(f"Text: {text}")
            print("-" * 100)
            print()

if arguments[0] == "new":
    title = arguments[1]  # TODO: Tratar exceptions
    text = [
        f"{title}",
        input("tag: ").strip(),
        input("text: \n").strip(),
    ]
    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")
