#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
# triangulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot
co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjacente: "))
print("O comprimento da hipotenusa é {:.2f}.".format(hypot(co, ca)))
