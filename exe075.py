
tupla = ()
tupla_par = ()
for c in range(1, 6):
    n = int(input('Digite um numero: '))
    tupla += (n,)
    if n % 2 == 0:
        tupla_par += (n,)



print(f'O numero 9 apareceu {tupla.count(9)} vezes!')
if 3 in tupla:
    print(f'O numero 3 apareceu a primeira vez na posição: {tupla.index(3) + 1}')
else:
    print(f'O Numero não existe na tupla!')
print(f'Os numeros pares são {tupla_par}')
