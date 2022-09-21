#!/usr/bin/env python3
"""Exemplos de envio de e-mail"""
import smtplib

SERVER = "localhost"
PORT = 8025

FROM = "fulano@gmail.com"
TO = ["destino@server.com", "outro@server.com"]
SUBJECT = "Meu e-mail via Python"
TEXT = """\
Este é o meu e-mail enviado pelo Python
<b>Olá Mundo!!!</b>
"""

# SMTP
message = f"""\
From: {FROM}
To: {", ".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, message.encode("utf-8"))
