print('-=' * 22)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 22)
# acumulador
cont = 0
# importando a biblioteca que fará o computador escolher um número
from random import randint
while True:
    jogador = int(input('Diga um valor: ')) # colhendo dados do jogador
    decisao = str(input('Par ou ímpar [P/I]? ')).strip().upper()
    computador = randint(0, 10) # fazendo o computador escolher um número entre 0 e 10
    calculo = (jogador + computador) % 2 # faz a soma do número e diz se é par ou não
    print('-=' * 25)
    # condições para o resultado de ambas as escolhas
    if decisao == 'P' and calculo == 0:
        print(f'Você digitou {jogador} e o computador {computador}. Total: {computador + jogador}.')
        print('PAR!')
        cont += 1 # contar quantas vezes o jogador venceu
    elif decisao == 'I' and calculo == 1:
        print(f'Você digitou {jogador} e o computador {computador}. Total: {computador + jogador}.')
        print('ÍMPAR!')
        cont += 1 # contar quantas vezes o jogador venceu
    else:
        print(f'Você digitou {jogador} e o computador {computador}. Total: {computador + jogador}.')
        print('PERDEU!')
        break # comando para interromper o programa quando o jogador perder
    print('-=' * 25)
# gambiarra para corrigir um erro de "você acertou 1 vezes" ou "0 vezes"
if cont == 1 or cont == 0:
    print(f'Fim de Jogo. Você venceu {cont} vezes.')
else:
    print(f'Fim de Jogo. Você venceu {cont} vezes.')