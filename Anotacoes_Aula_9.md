# Analise de Strings

## Comando len
Sintaxe: len(var)
Faz a leitura do tamnho total da variável

## Comando count
Sintaxe: var.count('algo')
Faz a contagem de um determinado caractere, é sensitive case.
É possivel fazer uma contagem com fatiamento:

Sintaxe:
var.count('algo',0,13).

## Comando find.
Sitaxe: var.find('algo')
Procura as Strings dentro da variavel, é sensitive case.

Obs: Quando fazemos uma busca que não encontrada nada, o resultado é "-1".

## Operador IN
Sintaxe: 'Algo' in frase.

# Transformações

## Comando replace
Sintaxe: var.replace('Algo, 'Algo')
Trocar de algo por outro.

## Maisculo, Minusculo, Capitalize etc...
Sintaxes:
var.upper()
var.lower()
var.capitalize() (primeira letra Maisculo)
var.title() (primeira leitura Maisculo checando os espaços)
var.strip() (remove todos os espaços inuteis)
var.rstrip() (remove pela direta)
var.lstrip() (remove pela esquerda)

#Divisões de Strings
Sintaxes:
var.split()
Faz uma divisao entre os espaço, refazendo um novo indice, fazendo uma nova lista

'separardor'.join(frase)

frase = 'Curso em Vídeo Python'
print(frase[3])
print(frase[3:13])
print(frase[13:])
print(frase[::2])
print(frase.upper()) #Colocar todas as letras em maiuculas
print(frase.upper().count('O')) #combina metodos - 1) Joga todos as frases para M, e depos conta.
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python', 'Android')) #Não muda efetivamente
"""
Muda efetivamente
frase = frase.replace('Python', 'Android')
print(frase)
"""
print(frase.find('Vídeo'))
print(frase.lower().find('vídeo'))

print(frase.split()) # Vira uma lista

dividido = frase.split()
print(dividido[2][3]) # mostra a frase dividia na lista 2, e a letra na posição 3.


print("""É possível escrer mais de 
uma linha usando (3 aspas no final e no inicio)""")


