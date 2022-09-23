#!/usr/bin/env python3

names = [
    "Carlos",
    "Joao",
    "Bruno",
    "Bernardo",
    "Barbara",
    "Brian",
]


# TODO: Usar lambdas


def starts_with_b(text):
    # return text[0].lower() == "b"
    return text.lower().startswith("b")


# for name in names:
#     if name.lower().startswith("b"):
#         print(name)

print(*list(filter(starts_with_b, names)), sep="\n")
