matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

soma = 0
somaTerceiraColuna = 0
maiorValorSegColuna = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor {linha}, {coluna}: '))

print(f'-='*30)
print(f'Matriz:')

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

# Resolvendo o problema dos valores pares:

for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz[linha][coluna] % 2 == 0:
            soma += matriz[linha][coluna]

for linha in range(0, 3):
    coluna = 2
    somaTerceiraColuna += matriz[linha][coluna]

for linha in range(0, 3):
    coluna = 1
    if matriz[linha][coluna] > maiorValorSegColuna:
        maiorValorSegColuna = matriz[linha][coluna]

print(f'-=' * 30)
print(f'A soma dos valores par é: {soma}')
print(f'A Soma a teceira coluna é: {somaTerceiraColuna}')
print(f'Maior valor da segunda coluna é: {maiorValorSegColuna}')
 