

a1 = int(input('Digite o primeiro termpo da PA: '))
r = int(input('Digite a razão da PA: '))
print(a1)
pa = 0
c = 1

while c < 10:
    c += 1
    pa = a1 + r
    a1 = pa
    print(pa)
