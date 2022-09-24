#!/usr/bin/env python3

contador = 0


def funcao():
    global contador
    contador += 1

    subcontador = 0

    def funcao_interna():
        global contador
        contador += 1

        nonlocal subcontador
        subcontador += 2

    funcao_interna()

funcao()
funcao()
funcao()

print(contador)
