from datetime import date

maior = 0
menor = 0

for c in range(1, 7+1):
    ano_nas = int(input(f'{c}ª Pessoa - Ano de Nascimento:  '))
    if date.today().year - ano_nas > 21:
        maior += 1
    else:
        menor += 1

print(f'Qtd maior de idade: {maior}')
print(f'Qtd menor de idade: {menor}')
