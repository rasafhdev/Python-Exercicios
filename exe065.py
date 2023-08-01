
opc = ''
numero_para_media = 0
lista_de_nDigitados = []
soma_dos_nDigitados = 0
while opc != 'N':
    n = int(input('Digite um um numero: '))
    lista_de_nDigitados.append(n)
    numero_para_media += 1
    soma_dos_nDigitados += n
    opc = str(input('Deseja Continuar? ')).upper()

print(f'Foram digitados {numero_para_media}')
print(f'A soma de todos numeros é igual = {soma_dos_nDigitados}')
print(f'Portanto, a média é igual a: {soma_dos_nDigitados/numero_para_media}')
print(f'Maior número digitado: {max(lista_de_nDigitados)}')
print(f'Menor número digitado: {min(lista_de_nDigitados)}')
