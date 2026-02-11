from time import sleep
from random import randint
print('Vamos jogar um jogo?')
print('Irei pensar em um número entre 0 e 5.')
print('Você deverá tentar adivinhar...')
print('Direi no final se ganhou ou perdeu.')
computador = randint(0, 5)
jogador = int(input('Digite um número entre 0 e 5: '))
if computador == jogador:
    print(f'PARABÉNS! Você me venceu!')
if computador != jogador:
    print(f'GANHEI! Você escolheu {jogador} e eu escolhi {computador}!')