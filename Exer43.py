# desenvolva um programa que calcule o IMC de uma pessoa e retorne seu status
# Abaixo de 18.5 = Abaixo do peso
# Entre 18.5 e 25 = Peso ideal
# 25 até 30 = Sobrepeso
# 30 até 40 = obesidade
# acima de 40 = obesidade morbida
import math

peso = float(input("Peso: "))
altura = float(input("Altura: "))
IMC = peso / altura**2
status = str
if IMC < 18.5:
    status = "\033[1;31mabaixo do peso\033[m."
elif 18.5 <= IMC < 25:
    status = "com \033[32mpeso ideal\033[m."
elif 25 <= IMC < 30:
    status = "com \033[33msobrepeso\033[m."
elif 30 <= IMC < 40:
    status = "com \033[1;33mobesidade\033[m."
else:
    status = "com \033[1;31mobesidade morbida\033[m."

print("Seu índice de massa corporal é \033[34m{:.2f}\033[m portando você está {}".format(IMC, status))