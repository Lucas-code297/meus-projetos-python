# programa que lê a frase pelo teclado e mostra:
# quantas vezes aparece a letra "A"
# quando aparece pela primeira vez
# quando aparece pela última vez
frase = str(input('Escreva um frase: ').upper())
# contando quantas vezes ela aparece
print(frase.count('A'))
# encontrada pela primeira vez
print(frase.find('A'))
# quando aparece pela última vez
print(frase.rfind('A'))