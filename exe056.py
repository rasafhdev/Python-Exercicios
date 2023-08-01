media = 0
homem_mais_velho = None
idade_homem_mais_velho = 0

qtd_menor_20 = 0

for c in range(1, 4+1):
    # Recebe os dados
    nome = str(input('Digite seu nome: '))
    idade = int(input('Sua idade: '))
    sexo = str(input('Sexo: [M/F]: ')).lower()

    # calcula média
    media += idade / 3

    # Verifica o homem mais velho
    if sexo == 'm':
        if homem_mais_velho is None or idade > idade_homem_mais_velho:
            homem_mais_velho = nome
            idade_homem_mais_velho = idade
    # Vefica quantas mulheres são menores de 20 anos
    elif sexo == 'f' and idade < 20:
        qtd_menor_20 += 1

# Output

print(f'Média das idades: {media:.2f}')
print(f'Nome do Homem mais velho: {homem_mais_velho}')
print(f'Quatidade de mulheres abaixo de 20 anos: {qtd_menor_20}')