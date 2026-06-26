tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
         'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um numero entre 0 e 20:'))
if n > 20 or n < 0:
    while True:
        n= int(input('Valor incorreto. Digite novamente: '))
        if n <= 20 and n >= 0:
            print(f'Você digitou o número {tupla[n]}.')
            break
else:
    print(f'Você digitou o número {tupla[n]}.')