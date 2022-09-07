#!/usr/bin/env python3

import os
import logging
from logging import handlers

# BOILERPLATE
# TODO: usar função
# TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

log = logging.Logger(__name__, level=log_level)

# ch = logging.StreamHandler()
# ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "meulog.log", maxBytes=10**6, backupCount=10
)
fh.setLevel(log_level)

fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s l:%(lineno)d "
    "f:%(filename)s: %(message)s"
)
fh.setFormatter(fmt)

log.addHandler(fh)

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
