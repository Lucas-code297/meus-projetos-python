# programa que lê um ângulo qualquer e mostra na tela o seu seno, cosseno e tangente desse ângulo
import math
a = float(input('Qual é o ângulo? '))
# passando os graus para números radianos
r = math.radians(a)
# calculando os números radianos em seno, cosseno e tangente
seno = math.sin(r)
cosseno = math.cos(r)
tangente = math.tan(r)
print('-' * 40)
print(f'O seno de {a} graus é {seno:.2f}!')
print(f'O cosseno de {a} graus é {cosseno:.2f}!')
print(f'A tangente de {a} graus é {tangente:.2f}!')
print('-' * 40)