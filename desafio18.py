#Faça um programa que leia um ângulo qualquer e mostre na tela o valor
# do seno, cosseno e tangente desse ângulo.
import math

angulo = float(input("Digite o ângulo: "))
s = math.sin(math.radians(angulo))
c = math.cos(math.radians(angulo))
t = math.tan(math.radians(angulo))
print("Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}".format(s, c, t))
