import math
angulo = float(input('Digite o ângulo que você deseja: '))
radians = math.radians(angulo)
print(f'O angulo de {angulo} tem o SENO de {math.sin(radians):.2f}')
print(f'O angulo de {angulo} tem o COSSENO de {math.cos(radians):.2f}')
print(f'O angulo de {angulo} tem a TANGENTE de {math.tan(radians):.2f}')