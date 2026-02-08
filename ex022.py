# criar um programa que lê o nome completo de uma pessoa e diz:
# o nome com todas as letras maiúsculas
# o nome com todas as letras minúsculas
# quantas letras ao todo (sem considerar os espaços)
# quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo, por gentileza: '))
nome = nome.strip()
print(f'Seu nome com todas as letras maiúsculas: {nome.upper()}')
print(f'Seu nome com todas as letras minúsculas: {nome.lower()}')
print(f'A quantidade de letras (sem contar os espaços): {len(nome) - nome.count(' ')}')
no = nome.split()
print(f'A quantidade de letras do seu primeiro nome: {len(no[0])}')