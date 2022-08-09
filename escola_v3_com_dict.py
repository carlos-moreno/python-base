#!/usr/bin/env python
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que frequentam cada uma das
atividades.
"""
__version__ = "0.1.0"
__author__ = "Carlos Moreno"

sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["João", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = {
    "Inglês": aula_ingles,
    "Música": aula_musica,
    "Dança": aula_danca,
}

for atividade, alunos in atividades.items():
    print(f"Lista de Alunos de {atividade}".center(55))
    print("#" * 55)
    atividade_sala1 = set(sala1) & set(alunos)
    atividade_sala2 = set(sala2) & set(alunos)

    print("Sala 1: ", atividade_sala1)
    print("Sala 2: ", atividade_sala2)
    print("-" * 55)
