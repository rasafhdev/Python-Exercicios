# Código 1:

pessoas_mais_18 = 0
homens_cadastrados = 0
mulher_menor_20 = 0

while True:
    idade = int(input('Sua idade: '))
    sexo = str(input('Sua seu [M/F]: ')).upper().strip()

    while sexo not in 'MF':
        print('Resposta invalida!')
        sexo = str(input('Sua seu [M/F]: ')).upper().strip()

    print('Registrado!\n')

    if idade > 18:
        pessoas_mais_18 += 1

    if sexo == 'M':
        homens_cadastrados += 1

    if sexo == 'F' and idade < 20:
        mulher_menor_20 += 1

    continua = str(input('Deseja continuar [S/N]: ')).upper().strip()

    while continua not in 'SN':
        print(f'Resposta Invalida')
        continua = str(input('Deseja continuar [S/N]: ')).upper().strip()

    if continua == 'N':
        break

print(f'Qtd pessoas +18 anos: {pessoas_mais_18}')
print(f'Qtd Homens cadastrados: {homens_cadastrados}')
print(f'Qtd Mulheres -20 anos: {mulher_menor_20}')
