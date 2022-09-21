#!/usr/bin/env python
"""Imprime a mensagem de um e-mail

NÂO MANDE SPAM!!!
"""
__version__ = "0.1.1"
__author__ = "Carlos Moreno"

import sys
import os
import smtplib
from email.mime.text import MIMEText

arguments = sys.argv[1:]
if not arguments:
    print("Informe os parametros necessarios.")
    sys.exit(1)
elif len(arguments) < 2:
    print("Informe os parametros conforme o exemplo abaixo:")
    print("python interpolacao.py `arquivo_emails` `arquivo_template_mensagem`")
    sys.exit(1)

emails_file = arguments[0]
template_file = arguments[1]

path = os.curdir
filepath = os.path.join(path, emails_file)
templatepath = os.path.join(path, template_file)

with smtplib.SMTP(host="localhost", port=8025) as server:
    for line in open(filepath):
        name, email = line.split(",")
        text = (
            open(templatepath).read()
            % {
                "nome": name,
                "produto": "caneta",
                "texto": "Escrever muito bem",
                "link": "https://canetaslegais.com",
                "quantidade": 1,
                "preco": 50.5,
            }
        )

        from_ = "beltrano@xpto.com"
        to = ", ".join([email])
        message = MIMEText(text)
        message["Subject"] = "Compre mais"
        message["From"] = from_
        message["To"] = to

        server.sendmail(from_, to, message.as_string())
