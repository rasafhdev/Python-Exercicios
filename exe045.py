import random

print(f'Vamos jogar Jokenpô?')

print("""Como jogar?
Digite
1 - Pedra
2 - Papel
3 - Tesoura
""")

user = int(input('Sua escolha: '))
if user == 1:
    print('Player: Pedra')
elif user == 2:
    print('Player: Papel')
elif user == 3:
    print('Player: Tesoura')

pc = (random.randint(1, 3))

if pc == 1:
    print('PC: Pedra')
elif pc == 2:
    print('PC: Papel')
elif pc == 3:
    print('PC: Tesoura')

# Compara gamer
print('--- RESULTADO ---')

if pc == user:
    print('Empate!')
# So pc jogar pedra e usuario papel: Usuário vence
elif pc == 1 and user == 2:
    print('Usuário Venceu!')
# Se pc jogar pedra e usuário tesoura: PC Venceu
elif pc == 1 and user == 3:
    print('PC Venceu!')
# Se pc jogar papel e usuário jogar pedra: PC Venceu
elif pc == 2 and user == 1:
    print('PC Venceu')
# Se pc jogar papel e usuário tesoura: Usuário venceu
elif pc == 2 and user == 3:
    print('Usuário venceu!')
# Se pc jogar tesoura e usuário pedra: Usuário Venceu
elif pc == 3 and user == 1:
    print('Usuário Venceu!')
# Se o pc jogar tesoura e usuário papel: PC Venceu
elif pc == 3 and user == 2:
    print('PC Venceu')
else:
    print('Entrada invalida!')