# Desenvolva um programa que pergunte a distância da viagem em Km.
# Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200Km e R$0,45 por viagens mais longas.

distancia = float(input("Distância da viagem: "))
if distancia <= 200:
    print("O valor da viagem é de R${:.2f}.".format(distancia * 0.5))
else:
    print("O valor da viagem é de R${:.2f}.".format(distancia * 0.45))
