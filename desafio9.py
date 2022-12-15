#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
from time import sleep
num = int(input("Digite um número: "))
c = 0
print("_"*10)
while c < 10:
    c = c+1
    print("{} x {:2} = {}".format(num, c, num * c))
    sleep(0.2)
print("_"*10)
