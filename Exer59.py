'''num1 = float(input("1º número: "))
num2 = float(input("2º número: "))
print("[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair")
menu = int(input("Selecione uma opção: "))

somar = num1 + num2
multiplicar = num1 * num2
maior = float
if num1 > num2:
    maior = num1
elif num2 > num1:
    maior = num2
elif num1 == num2:
    maior = "igual"
sair = False

while not sair:
    if menu == 1:
        print(somar)
        num1 = float(input("1º número: "))
        num2 = float(input("2º número: "))
        print("[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair")
        menu = int(input("Selecione uma opção: "))
    if menu == 2:
        print(multiplicar)
        num1 = float(input("1º número: "))
        num2 = float(input("2º número: "))
        print("[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair")
        menu = int(input("Selecione uma opção: "))
    if menu == 3:
        print(maior)
        num1 = float(input("1º número: "))
        num2 = float(input("2º número: "))
        print("[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair")
        menu = int(input("Selecione uma opção: "))
        if num1 > num2:
            maior = num1
        elif num2 > num1:
            maior = num2
        elif num1 == num2:
            maior = "igual"
    if menu == 5:
        sair = True
    if menu == 4:
        num1 = float(input("1º número: "))
        num2 = float(input("2º número: "))
        print("[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair")
        menu = int(input("Selecione uma opção: "))
'''

num1 = float(input("1º número: "))
num2 = float(input("2º número: "))
choice = 0
while choice != 5:
    print("[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair")
    choice = int(input("Escolha opção: "))
    if choice == 1:
        print(num1 + num2)
    if choice == 2:
        print(num1 * num2)
    if choice == 3:
        if num1 > num2:
            print(f"{num1} é maior.")
        elif num2 > num1:
            print(f"{num2} é maior.")
        elif num1 == num2:
            print("Igual.")
    if choice == 4:
        num1 = float(input("1º número: "))
        num2 = float(input("2º número: "))
        print("[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair")
        choice = int(input("Escolha opção: "))
    if choice == 5:
        print("Programa encerrado.")
