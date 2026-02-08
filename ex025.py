# programa que lê o nome da pessoa e diz se tem "Silva" no nome
nome = str(input('Digite o seu nome completo por gentileza: '))
nome = nome.title()
print(f'Tem "Silva" no nome? {'Silva' in nome}')