#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10."""
__version__ = "0.1.1"
__author__ = "Carlos Moreno"


numeros = list(range(1, 11))

for n1 in numeros:
    print("\n{:-^26}".format(f"Tabuada do número {n1}"))
    print()
    for n2 in numeros:
        resultado = n2 * n1
        print("{:^26}".format(f"{n2} x {n1} = {resultado}"))
    print("#" * 25)
