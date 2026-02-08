# programa que lê uma frase e diz se ela é um palíndromo
frase = str(input('Digite uma frase: ')). strip(). upper()
p = frase.split()
j = ''.join(p)
inverso = ''
for letra in range(len(j) - 1, -1, -1):
    inverso += j[letra]
if inverso == j:
    print(f'A frase {frase} é um palíndromo.')
else:
    print(f'A frase {frase} não é um palíndromo.')