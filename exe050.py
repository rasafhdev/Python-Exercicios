print('Digigite 6 numeros inteiros')

soma = 0

for c in range(1, 6+1):
    n = int(input(f'{c}º numero: '))
    if n % 2 == 0:
        soma += n
print(f'A soma dos numeros pares resultou em: {soma}')
