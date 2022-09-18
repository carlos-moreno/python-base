#!/usr/bin/env python3
""" Repete vogais

Faça um programa que pede ao usuário que digite uma ou mais palavras e 
imprime cada uma das palavras com suas vogais duplicadas.

ex:
python repete_vogais.py
'Digite uma palavra (ou enter para sair): ' Python
'Digite uma palavra (ou enter para sair): ' Bruno
'Digite uma palavra (ou enter para sair): ' >enter>
Pythoon
Bruunoo
"""

words = []
while True:
    word = input("Digite uma palavra (ou enter para sair): ")
    if not word:
        break
    final_word = ""
    for letter in word:
        # TODO: Remover acentuação usando função
        final_word += letter * 2 if letter.lower() in "aeiou" else letter
    words.append(final_word)

print(*words, sep="\n")
