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
