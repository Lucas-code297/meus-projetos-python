# programa que lê o nome completo da pessoa, mostrando em seguida o seu primeiro e último nome separadamente
nome = str(input('Digite seu nome completo, por gentileza: ')). strip()
nome = nome.split()
print('Prazer em te conhecer!')
# primeiro nome da pessoa
print(f'Seu primeiro nome é {nome[0]}!')
# último nome da pessoa
print(f'Seu último nome é {nome[len(nome)-1]}!')
