#!/usr/bin/env python3
"""Imprime apenas os nomes iniciados com a letra B"""

names = [
    "Carlos",
    "Joao",
    "Bruno",
    "Bernardo",
    "Barbara",
    "Brian",
]


# Estilo funcional
print("Estilo funcional")
print(
    *list(filter(lambda text: text.lower().startswith("b"), names)), sep="\n"
)

print()

# Estilo procedural
print("Estilo procedural")
def starts_with_b(text):
    """Return bool if text starts with b"""
    return text.lower().startswith("b")


filtro = filter(starts_with_b, names)
filtro = list(filtro)
for name in filtro:
    print(name)
