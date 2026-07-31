# gerar 5 valores, colocá-los em uma tupla e dizer qual é o menor e qual é o menor

from random import randint
# gerandos os 5 valores aleatórios dentro da tupla
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))
print(f'Os 5 valores digitados foram: ', end='')
# tirando os parênteses
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi: {max(numeros)}')
print(f'O menor valor sorteado foi: {min(numeros)} ')
