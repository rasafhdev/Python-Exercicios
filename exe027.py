print("""Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último
nome separadamente.
Ex: Ana Maria de Souza
Primeiro: Ana
#Segundo: Souza""")

"""
nome = input('Nome completo: ').split()
print(f"""
#Primeiro nome: {nome[0]}
#Segundo nome: {nome[-1]}
""")
"""
def verifica_nome(nome):

    #Vericica primeiro nome
    primeiro_nome = nome[0]

    #verifica segundo_nome
    ultimo_nome = nome[-1]

    return primeiro_nome, ultimo_nome

# Faz solicitação do nome

nome = input('Digite seu nome completo: ').split()

# chama o metodo
primeiro_nome, ultimo_nome = verifica_nome(nome)

print(f"""
Primeiro nome: {primeiro_nome}
Segundo nome: {ultimo_nome}
""")
