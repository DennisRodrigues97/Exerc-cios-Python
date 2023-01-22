def menu():
    num1 = float(input("1º número: "))
    num2 = float(input("2º número: "))
    print("[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair")
    menu1 = int(input("Selecione uma opção: "))

controle = False

while not controle:
    menu()
    if menu() == 5:
        controle = True