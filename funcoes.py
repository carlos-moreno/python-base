#!/usr/bin/env python3
"""Exemplos de funções"""
from math import sqrt

"""
f(x) = 5 * (x / 2)
"""

# Solid - Single Responsibility

def f(x): # assinatura
    result = 5 * (x / 2)
    return result

print(f(10) == 25)


def double(x):
    return x * 2

valor = double(f(10))

print(valor)
print(valor == 50)

def print_in_upper(text):
    """Procedure with no explicit return"""
    print(text.upper())
    # implicit return None

print(print_in_upper("carlos augusto"))

####

def heron(a, b, c):
    """Calcula a area de um triangulo com areas diferentes"""
    perimeter = a + b + c
    s = perimeter / 2
    area = s * (s - a) * (s - b) * (s - c)
    return sqrt(area) # area ** 0.5


def heron2(params):
    return heron(*params)

triangulos = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37),
]

for t in triangulos:
    area = heron(*t)
    print(f"A Area do triangulo é: {area}")
