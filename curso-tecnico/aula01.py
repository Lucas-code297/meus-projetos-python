# acumuladores para contar veículos estacionados (por tipo)
cont_a = cont_b = cont_c = cont_d = 0
#calcular quanto foi arrecadado
arrecadado_total = 0
# usarei o tempo como um intervalo de uma anotação para outra
from time import sleep
# saber qual é o dia da semana
dia = str(input('Qual é o dia da semana?')).strip().title()
if dia == 'Domingo':
    print('Desculpe. O UniCesumar Parking não funciona nesse dia.')
    print('Retorne novamente amanhã.')
else:
    # validação do horário para funcionamento do estacionamento
    hora = 8
    while True:
        hora = int(input('Em que horário está estacionado\n(digite apenas números inteiros)? '))
        # condição de funcionamento: 8h às 18h
        if 8 <= hora <= 18:
            # que tipos de veiculos estão no estacionamento
            veiculos = str(input('Qual é o tipo de veículo estacionado? ')).strip().title()
            # não permitir a entrada de veículos não autorizados
            if veiculos != 'Carro' and veiculos != 'Motocicleta' and veiculos != 'Camionete':
                print('Desculpe, esse tipo de veículo não é permitido em nosso estacionamento.')
            else:
                # tempo que o veiculo ficou no estacionamento
                tempo = int(input('Quantos minutos o veículo esteve estacionado? '))
                # valor a pagar pelo tempo no estacionamento
                if tempo <= 15:
                    # controle da quantidade de veículos isentos do pagamento
                    cont_d += 1
                    print('Certo. De acordo com o tempo, você ficou isento do pagamento!')
                elif tempo < 60:
                        # tempo cobrado de 16 a 60 minutos.
                        valor_a = 1.50
                        arrecadado_total += valor_a # adiciona ao total
                        print(f'Certo. De acordo com o tempo, você deve pagar R${valor_a:.2f}.')
                else:
                    # cobra de permânencia adicional
                    valor_b = 1.50
                    # calculo do tempo que passou
                    tempo_restante = tempo - 60
                    while tempo_restante > 0:
                        valor_b += 1.00
                        tempo_restante -= 60
                    arrecadado_total += valor_b
                    print(f'Certo. De acordo com o tempo, você deve pagar R${valor_b:.2f}.')
                if veiculos == 'Carro':
                    cont_a += 1
                elif veiculos == 'Motocicleta':
                    cont_b += 1
                else:
                    cont_c += 1
        else:
            # se a hora for menor que 8h ou maior que 18h, o expediente encerra
            print('Desculpe, não funcionamos nesse horário.')
            print('Funcionamos das 8h às 18h.')
            break
        print('-=' * 20)
        sleep(2)
sleep(1)
print(f'Ao todo, tivemos {cont_a} carros, {cont_b} motos e {cont_c} camionetes estacionados.')
sleep(1)
print(f'O valor arrecadado total é R${arrecadado_total:.2f}.')
sleep(1)
print(f'Ao todo, {cont_d} veículos estiveram isentos do pagamento.')
sleep(1)
print('Expediente finalizado.')