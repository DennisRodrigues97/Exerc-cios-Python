# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.
import random

vel = random.uniform(0, 200)
multa = ((vel - 80).__abs__()) * 7
print("### Velocidade máxima 80 Km/h. ###\n")
if vel > 80:
    print("Sua velocidade foi {:.2f} Km/h e por isso você foi multado!".format(vel))
    print("O valor da multa é {:.2f}".format(multa))
else:
    print("Parabéns, sua velocidade foi {:.2f} Km/h e você andou dentra da velocidade permitida.".format(vel))
