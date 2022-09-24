#!/usr/bin/env python

# aqui começa o escopo global
nome = "Global"

def funcao():
    # aqui começa o escopo local da função
    nome = "Local"

    def funcao_interna(): # inner function
        # aqui começa o escopo local da função interna
        nome = "Interna"
        # print("Escopo local da função interna:", locals())
        # print("#" * 50)
        print(nome)
        return nome
        # aqui termina o escopo local da função interna

    # print("Escopo local da função:", locals())
    # print("=" * 50)
    funcao_interna()
    print(nome)
    return nome
    # aqui termina o escopo local da função

# print("Escopo global do programa:", globals())
# print("-" * 50)
funcao()
print(nome)

# aqui termina o escopo global
