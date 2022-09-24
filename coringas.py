#!/usr/bin/env python3


def funcao(*args, timeout=10, **kwargs):
    print(args)
    print(kwargs)
    print(f"timeout = {timeout}")


funcao(
    "Carlos", 
    1, 
    True, 
    [], 
    (), 
    nome="Augusto", 
    cidade="Rio Branco", 
    timeout=5
)
