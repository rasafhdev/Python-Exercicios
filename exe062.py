

a1 = int(input('Digite o primeiro termpo da PA: '))
r = int(input('Digite a razão da PA: '))
print(a1)
pa = 0
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(pa)
        c += 1
        pa = a1 + r
        a1 = pa
    print('Pausa')
    mais = int(input('Quer mostrar mais quantos termos ? Para terminar: [0]'))
print(f'Fim')
