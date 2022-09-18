#!/usr/bin/env python3
""" Reserva de quarto

Faça um programa de terminal que exibe ao usuário uma lista dos quartos 
disponíveis para alugar e o preço de cada quarto, esta informação está 
disponível em um arquivo de texto separado por vírgulas.

`quartos.txt`
# codigo, nome, preço
1, Suíte Master, 500
2, Quarto Família, 200
3, Quarto Single, 100
4, Quarto Simples, 50


O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado
e a quantidade de dias e no final exibe o valor estimado a ser pago.

O programa deve salvar esta escolha em outro arquivo contendo as reservas

`reservas.txt`
# cliente, quarto, dias
Bruno, 3, 12


Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma
mensagem informando que já está reservado.
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

ocupados = {}
try:
    for line in open("reservas.txt"):
        nome, quarto, quantidade_dias = line.strip().split(",")
        ocupados[int(quarto)] = {
            "nome": nome,
            "quantidade_dias": int(quantidade_dias),
        }

except FileNotFoundError:
    log.error("Arquivo não existe!")
    sys.exit(1)

quartos = {}
try:
    for line in open("quartos.txt"):
        codigo, nome, preco = line.strip().split(",")
        quartos[int(codigo)] = {
            "nome": nome,
            "preco": float(preco),  # TODO: Decimal
            "disponivel": False if int(codigo) in ocupados else True,
        }

except FileNotFoundError:
    log.error("Arquivo não existe!")
    sys.exit(1)

print("Reserva no Hotel Pythonico da Linux Tips")
print("-" * 52)
if len(ocupados) == len(quartos):
    print(f"Hotel Lotado \U0001F6D1")
    sys.exit(1)

nome = input("Nome do Cliente: ").strip()
print("Lista de quartos:")
for codigo, dados in quartos.items():
    nome_quarto = dados["nome"]
    preco = dados["preco"]
    disponivel = "\U0001F6AB" if not dados["disponivel"] else "\U00002705"
    print(f"{codigo}: {nome_quarto} - R$ {preco:.2f} - {disponivel}")

print("-" * 52)

try:
    quarto = int(input("Número do quarto: ").strip())
    if not quartos[quarto]["disponivel"]:
        print(f"O quarto {quarto} não está disponível.")
        sys.exit(1)
except ValueError:
    log.error("Número inválido, digite apenas digitos.")
    sys.exit(1)
except KeyError:
    log.error("O quarto %s não existe", quarto)
    sys.exit(1)

try:
    quantidade_dias = int(input("Quantidade de dias: ").strip())
except ValueError:
    log.error("Número inválido, digite apenas digitos.")
    sys.exit(1)

nome_quarto = quartos[quarto]["nome"]
preco_quarto = quartos[quarto]["preco"]
total = preco_quarto * quantidade_dias

with open("reservas.txt", "a") as file_:
    file_.write(f"{nome},{quarto},{quantidade_dias}\n")

print(f"{nome} você escolheu o {nome_quarto} e vai custar R$ {total:.2f}")
