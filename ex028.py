# fazer um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar adivinhar o número escolhido pelo pc
# o programa deve mostrar na tela se o usuário venceu ou perdeu
from random import randint
from time import sleep
print('Vou pensar em um número entre 0 e 5!')
sleep(2)
print('Você deve adivinhar que número escolhi, direi se venceu ou perdeu!')
sleep(2)
num = int(input('Digite um número de 0 a 5: '))
escolhido = randint(0, 5)
print('Pensando...')
sleep(3)
if num == escolhido:
    print(f'PARABÉNS! O número escolhido foi {escolhido}, você venceu o jogo!')
else:
    print(f'Haha! Eu te venci, o número escolhido foi {escolhido}!')
