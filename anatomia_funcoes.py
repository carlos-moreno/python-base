#!/usr/bin/env python3
"""Este módulo serve apenas para anotação"""

# definição ou atribuição
# assinatura + type hints
# documentação / docstring
# codigo
# valor de retorno

# - parametros
# posicional => passados em ordem


def nome_da_funcao(a, b, c):
    """Esta função faz algo com a, b e c.

    Use esta função quando quiser a + b + c

    >>> nome_da_funcao(1, 2, 3)
    6

    :param a: Número inteiro
    :param b: Número inteiro
    :param c: Número inteiro
    :return: Retorna o resultado de a + b + c
    """
    resultado = a + b + c
    return resultado


# passagem de argumentos
valor = nome_da_funcao(1, 2, 3)

# passagem de argumentos nomeados
valor = nome_da_funcao(a=1, b=2, c=3)
valor = nome_da_funcao(a=1, c=2, b=3)

# passagem de argumentos mista
valor = nome_da_funcao(1, 2, c=3)
valor = nome_da_funcao(1, c=2, b=3)

# função com muitos argumentos
valor = nome_da_funcao(a=1, b=2, c=3)

print(valor)

########################


def outra_funcao(a, b, c):
    """Explica o que a função faz"""
    # tupla como valor de retorno
    return a * 2, b * 2, c * 2


valor1, valor2, valor3 = outra_funcao(1, 2, 3)
print(valor1)
print(valor2)
print(valor3)

valor1, *resto = outra_funcao(1, 2, 3)
print(valor1)
print(resto)

########################

# Passagen de argumentos com desempacotamento


def soma(n1, n2):
    """Faz a soma de 2 números"""
    return n1 + n2


# normal
print(soma(10, 20))

# argumentos em sequencia / posicional
args = (20, 30)
# print(soma(args[0], args[1]))
print(soma(*args))

# argumentos dicionario / nomeados

args = {"n2": 90, "n1": 100}  # dict, hashmap
# print(soma(n1=args["n1"], n2=args["n2"]))
print(soma(**args))

###########################

lista_de_valores_para_somar = [
    {"n2": 90, "n1": 110},
    {"n2": 80, "n1": 200},
    {"n1": 350, "n2": 100},
    (5, 10),
    [8, 13],
]

for item in lista_de_valores_para_somar:
    if isinstance(item, dict):
        print(soma(**item))
    else:
        print(soma(*item))
