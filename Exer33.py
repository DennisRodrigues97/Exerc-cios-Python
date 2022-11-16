# Faça um programa que leia 3 números e diga qual é o maior e qual é o menor.

print("### Diga três números ###")
num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))
num3 = float(input("Terceiro número: "))

maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

print("O maior número é o {} e o menor é {}.".format(maior, menor))
