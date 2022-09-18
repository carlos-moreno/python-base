#!/usr/bin/env python3
""" Alarme de temperatura

Faça um script que pergunta ao usuário qual a temperatura atual e o índice de 
umidade do ar, sendo que caso será exibida uma mensagem de alerta dependendo 
das condições.

temp maior 45: ALERTA!!! Perigo calor extremo
temp vezes 3 for maior ou igual a umidade: ALERTA!!! Perigo de calor úmido
temp entre 10 e 30: Normal
temp < 0: ALERTA: Frio extremo
"""
import sys
import os
import logging
from logging import handlers

# BOILERPLATE
# TODO: usar função
# TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

log = logging.Logger("alerta.py", level=log_level)

ch = logging.StreamHandler()
ch.setLevel(log_level)

fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s l:%(lineno)d "
    "f:%(filename)s: %(message)s"
)
ch.setFormatter(fmt)

log.addHandler(ch)

info = {
    "temperatura": None,
    "umidade": None
}

while True:
    info_size = len(info.values())
    filled_size = len([value for value in info.values() if value is not None])

    if info_size == filled_size:
        break

    for key in info.keys():
        if info[key] is not None:
            continue
        try:
            info[key] = float(input(f"Qual a {key}? ").strip())
        except ValueError:
            log.error("%s inválida, digite números", key)
            sys.exit(1)

temperatura, umidade = info.values()

if temperatura > 45:
    print("ALERTA!!! Perigo de calor extremo \U0001F975")
elif temperatura > 30 and (temperatura * 3) >= umidade:
    print("ALERTA!!! Perigo de calor úmido \U0001F975 \U00002652")
elif 10 <= temperatura <= 30:
    print("Normal \U0001F603")
elif 0 <= temperatura < 10:
    print("Frio \U0001F976")
elif temperatura < 0:
    print("ALERTA: Frio extremo \U00002603")
