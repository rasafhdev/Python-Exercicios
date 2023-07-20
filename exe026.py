"""
print("""#Faça um programa que leia uma frase do tecllado e mostre:
#1) Quantas vezes aparece a letra "A".
#2) Em que posição ela parece a primeira vez.
#3) Em que posição ela aparece a ultima vez.
""")

frase = str(input('Digite uma frase: ')).lower()
print(f"""
#1) Quantidade letra A: {frase.count("a")}
#2) Primeira posição: {frase.find("a")}
#3) Ultima posição: {frase.rfind("a")}
""")

"""
#Versão 2

def contar_letra_a(frase):
    # conta todas as letras A
    conta_a = frase.count("a")

    # primeira posição em que aparece
    primeira_ocorrencia = frase.find('a')

    # ultima posição em que aparece
    ultima_ocorrencia = frase.rfind('a')

    return conta_a, primeira_ocorrencia, ultima_ocorrencia

# Solicita entrada de dados
frase = str(input('Digite um frase: ')).lower().strip()

#Chama a função
conta_a, primeira_ocorrencia, ultima_ocorrencia = contar_letra_a(frase)

#Resutlados

print(f'Quantidade letras A: {conta_a}')
print(f'Primeira posição: {primeira_ocorrencia}')
print(f'Ultima Posição: {ultima_ocorrencia}')

