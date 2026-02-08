# jokenpô
from time import sleep
from random import choice
print('Vamos jogar jokenpô!')
sleep(1)
print('Você deve escolher entre: pedra, papel ou tesoura!')
sleep(2)
print('Farei o mesmo e assim veremos que ganhará o jogo!')
sleep(2)
jogador = str(input('Pedra, papel ou tesoura? ')). strip()
jogador = jogador.title()
lista = ['Pedra', 'Tesoura', 'Pedra']
computador = choice(lista)
if jogador == 'Tesoura' and computador == 'Pedra':
    print(f'GANHEI! Você escolheu {jogador} e eu escolhi {computador}!')
elif jogador == 'Tesoura' and computador == 'Papel':
    print(f'PERDI! Você escolheu {jogador} e eu escolhi {computador}!')
elif jogador == 'Pedra' and computador == 'Papel':
    print(f'GANHEI! Você escolheu {jogador} e eu escolhi {computador}!')
elif jogador == 'Pedra' and computador == 'Tesoura':
    print(f'PERDI! Você escolheu {jogador} e eu escolhi {computador}!')
elif jogador == 'Papel' and computador == 'Tesoura':
    print(f'GANHEI! Você escolheu {jogador} e eu escolhi {computador}!')
elif jogador == 'Papel' and computador == 'Pedra':
    print(f'PERDI! Você escolheu {jogador} e eu escolhi {computador}!')
elif jogador == computador:
    print(f'EMPATE! Você escolheu {jogador} e eu escolhi {computador}!')
else:
    print('Escolha uma das opções!')
print('Pronto para mais uma rodada?')
