print('Crie um programa que leia o nome de uma cidade e diga se ela começa ou com o nome "SANTO"')

nome_cidade = str(input("Digite o nome da sua cidade: ")).upper().strip()
print(nome_cidade[:5] == 'SANTO')
