import random
from time import sleep
num = random.randint(0, 5)
cont = 0
user = int(input("Adivinhe que número o computador escolheu entre 0 a 5: "))
print("Processando...")
sleep(0)
while user != num:
    if user > num:
        print("Menos!")
    elif user < num:
        print("Mais!")
    user = int(input("Tente novamente!\nEscolha um número entre 0 a 5: "))
    print("Processando ...")
    sleep(0)
    cont += 1
if num == user:
    print(f"Você acertou!!! O número escolhido foi {num}")
    print(f"Foram necessárias {cont} tentativas para você acertar.")
'''
Solução criada após a aula do Prof. Guanabara.
Utilizando um boleano como variável de controle o programa fica melhor, mais legivel. 
import random
from random import randint

computador = random.randint(0, 10)
resultado = False
contador = 0

while not resultado:
    usuario = int(input("Advinhe qual número o computador pensou: "))
    contador += 1
    if computador == usuario:
        resultado = True
    else:
        if computador > usuario:
            print("Mais...")
        elif usuario > computador:
            print("Menos...")
print(f"Parabéns, você acertou em {contador} tentativas.")'''