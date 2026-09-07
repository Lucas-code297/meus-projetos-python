# coletando a variável
n = str(input('Digite algo: '))
# dissecando a variável
print(type(n))
print(f'Só tem espaços? {n.isspace()}')
print(f'É um número? {n.isnumeric()}')
print(f'É alfabético? {n.isalpha()}')
print(f'É alfanumérico? {n.isalnum()}')
print(f'Está em minúsculas? {n.islower()}')
print(f'Está em maiúsculas? {n.isupper()}')
print(f'Está capitalizada? {n.istitle()}')