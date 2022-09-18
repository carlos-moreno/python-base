#!/usr/bin/env python3
""" Faça um programa que imprime os números pares de 1 a 200

ex.:
`python numeros_pares.py`
2
4
6
8
...
"""

for item in range(2, 201):
    if item % 2 == 0:
        print(item)
