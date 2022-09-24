#!/usr/bin/env python3


def transforma_em_maiusculo(texto):
    return texto.upper()


def transforma_em_minusculo(texto):
    return texto.lower()


def divide_por_2(numero):
    return numero // 2


# e nossa função principal


def faz_algo(valor, funcao):
    print(f"Aplicando {funcao} em {valor}")
    return funcao(valor)

names = ["Bruno", "João", "Bernardo", "Cintia", "Marcia", "Juca"]

print(sorted(names, key=len))

print(sorted(names, key=lambda name: name.count("i")))

print(sorted(names, key=lambda name: name.count("i"), reverse=True))

print(list(filter(lambda name: name.lower().startswith("b"), names)))

print(list(map(lambda name: "Hello " + name, names)))

# Calculadora

operacao = input("operação [sum, mul, div, sub]: ").strip()
n1 = float(input("n1: ").strip())
n2 = float(input("n2: ").strip())

operacoes = {
    "sum": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b,
}

resultado = operacoes[operacao](n1, n2)

print(f"O resultado é: {resultado:.2f}")
