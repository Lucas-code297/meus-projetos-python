# jogo de adivinhação
count = 0
from time import sleep
from random import randint
print('Irei pensar em um número entre 0 e 10!')
sleep(1)
print('Você deve adivinhar este número!')
sleep(1)
print('O jogo só acabará quando você adivinhar este número!')
sleep(1)
computador = randint(1, 10)
jogador = int(input('Qual é o seu palpite? '))
while jogador != computador:
    if jogador > computador:
        print('Menos... tente novamente.')
        jogador = int(input('Qual é o seu palpite?'))
        count = count + 1
    if jogador < computador:
        print('Mais... tente novamente.')
        jogador = int(input('Qual é o seu palpite?'))
        count = count + 1
    if jogador == computador:
        count = count + 1
print(f'Parabéns! Você acertou com {count} tentativas.')