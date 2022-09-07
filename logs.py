#!/usr/bin/env python3

import os
import logging

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

"""
log.debug("Mensagem para o DEV, QE, SYSADMIN")
log.info("Mensagem geral para os Usuários")
log.warning("Mensagem de aviso que não causa erro")
log.error("Mensagem de erro que afeta uma única execução")
log.critical("Mensagem que afeta o uso geral do sistema")
"""

print("------")

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))
