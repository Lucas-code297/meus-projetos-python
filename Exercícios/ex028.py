from time import sleep
from random import randint
print('Vamos jogar um jogo?')
sleep(1)
print('Irei pensar em um número entre 0 e 5.')
sleep(2)
print('Você deverá tentar adivinhar...')
sleep(2)
print('Direi no final se ganhou ou perdeu.')
sleep(2)
computador = randint(0, 5)
jogador = int(input('Digite um número entre 0 e 5: '))
if computador == jogador:
    print(f'PARABÉNS! Você me venceu!')
if computador != jogador:
    print(f'GANHEI! Você escolheu {jogador} e eu escolhi {computador}!')