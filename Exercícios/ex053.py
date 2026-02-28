frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'A frase "{frase}", de traz para frente é "{inverso}".', end=' ')
if inverso == junto:
    print('\nPortanto, é um palíndromo!')
else:
    print('\nPortanto, não é um palíndromo.')