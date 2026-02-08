# programa que lê a largura e a altura de uma parede em metros, calcula a sua área
# e diz quantos litros de tintas são necessário para pintá-la
# sabendo que cada litro de tinta pinta uma área de 2m²
largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura de uma parede? '))
r = (largura * altura)
l = r / 2
print(f'Certo! A parede tem {altura}m² de altura e {largura}m² de largura. \nPortanto, será necessário {l}l de tinta pintá-la!')