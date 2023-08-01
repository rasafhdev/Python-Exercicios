frase = str(input('Digite uma frase: ')).replace(' ', '').lower()

e_paplindromo = True
for c in range(len(frase)):
    if frase[c] != frase[-c - 1]:
        e_paplindromo = False
        break

if e_paplindromo:
    print(f'É Palindromo')
else:
    print(f'Não é Palindromo')
