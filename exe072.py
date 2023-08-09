n = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    n_usuario = int(input('Digite um numero: '))
    if n_usuario < 0 or n_usuario > 20:
        print('Tente novamente!', end=' ')
        continue
    else:
        print(f'Você digitou: {n[n_usuario]}')
        break
