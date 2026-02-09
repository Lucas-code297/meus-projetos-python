largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
área = altura * largura
print(f'Sua parede tem uma dimensão de {largura}x{altura}\n'
      f'e sua área tem {área}m²')
print(f'Serão necessários {área / 2}l de tinta para pintar a parede.')