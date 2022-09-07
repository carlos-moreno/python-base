#!/usr/bin/env python
"""Calculador infix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py
operação: sum
n1: 5
n2: 4
9

Os resultados serão salvos em `infixcalc.log`
"""
__version__ = "0.1.1"
__author__ = "Carlos Moreno"

import os
import sys
import logging

from datetime import datetime

# BOILERPLATE
# TODO: usar função
# TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

log = logging.Logger(__name__, level=log_level)

ch = logging.StreamHandler()
ch.setLevel(log_level)

fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s l:%(lineno)d "
    "f:%(filename)s: %(message)s"
)
ch.setFormatter(fmt)

log.addHandler(ch)

arguments = sys.argv[1:]

if not arguments:
    operation = input("operação: ")
    n1 = input("n1: ")
    n2 = input("n2: ")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    log.error("Número de argumentos inválidos. Tente `sum 5 5`")
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", "div")
if operation not in valid_operations:
    log.error(
        "Operação inválida. Tente usar uma das opções %s", valid_operations
    )
    sys.exit(1)

validated_nums = []
for num in nums:
    # TODO: Repetição while + exceptions
    if not num.replace(".", "").isdigit():
        log.error("Número inválido: %s", num)
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

try:
    n1, n2 = validated_nums
except ValueError as e:
    log.error(str(e))
    sys.exit(1)

# TODO: Usar dict de funções
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div" and n2 > 0:
    result = n1 / n2
elif operation == "div" and n2 <= 0:
    result = "Operação inválida -> divisão por zero"

path = os.curdir
filepath = os.path.join(path, "infixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv("USER", "guest")

print(f"{result}")

try:
    with open(filepath, "a") as file_:
        file_.write(
            f"{timestamp} - {user} -->  {operation}, {n1}, {n2} = {result}\n"
        )
except PermissionError as e:
    log.error(
        str(e),
    )
    sys.exit(1)
