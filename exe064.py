
soma_numeros = 0
n = 0
total_numeros_dig = 0
while n != 999:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    else:
        total_numeros_dig += 1
        soma_numeros += n

print(f'Total de numeros digitados {total_numeros_dig}')
print(f'Total da soma entre os numeros {soma_numeros}')

