from random import randint
from time import sleep
print('Vamos jogar um jogo?')
sleep(1)
print('Irei escolher entre pedra, papel, e tesoura.')
sleep(2)
print('Faça sua escolha e veremos quem ganha!')
sleep(1)
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
print('Suas opções: [0] Pedra;\n'
      '[1] Papel;\n'
      '[2] Tesoura.')
jogador = int(input('Digite o número de acordo com a sua jogada: '))
if computador == 0: #pedra
      if jogador == 0:
            print(f'EMPATE! Você jogou {itens[jogador]} e eu joguei {itens[computador]}!')
      elif jogador == 1:
            print(f'VOCÊ VENCEU! Você jogou {itens[jogador]} e eu joguei {itens[computador]}!')
      elif jogador == 2:
            print(f'VOCÊ PERDEU! Você jogou {itens[jogador]} e eu joguei {itens[computador]}!')
elif computador == 1: #papel
      if jogador == 0:
            print(f'VOCÊ PERDEU! Eu escolhi {itens[computador]} e você escolheu {itens[jogador]}!')
      elif jogador == 1:
            print(f'EMPATE! Você jogou {itens[jogador]} e eu joguei {itens[computador]}!')
      elif jogador == 2:
            print(f'VOCÊ GANHOU! Eu joguei {itens[computador]} e você jogou {itens[jogador]}!')
elif computador == 2: #tesoura
      if jogador == 0:
            print(f'VOCÊ GANHOU! Eu joguei {itens[computador]} e você jogou {itens[jogador]}!')
      elif jogador == 1:
            print(f'VOCÊ PERDEU! Eu joguei {itens[computador]} e você jogou {itens[jogador]}!')
      elif jogador == 2:
            print(f'EMPATE! Você jogou {itens[jogador]} e eu joguei {itens[computador]}!')