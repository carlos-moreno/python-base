#!/usr/bin/env python3

import time

def imprime_nome(nome, sobrenome="Moreno"):
    print(f"Seu nome é {nome} {sobrenome}")

imprime_nome("Carlos", "Moreno")
imprime_nome("Eleana")
imprime_nome("Isabella")
imprime_nome("Luíz Gabriel")


def conecta(host, timeout=10):
    print(f"conectando com {host}")
    for i in range(1, timeout + 1):
        time.sleep(1)
        print("." * i)
    print("erro ao conectar")

conecta("localhost", 5)
conecta("localhost")