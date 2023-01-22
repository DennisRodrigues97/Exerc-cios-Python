
inicio = 0 #int(input("Primeiro número: "))
segundo = 1 #inicio + 1 #int(input("Segundo número: "))
qtd = int(input("Quantidade de números da sequência: "))

while qtd > 0:
    print(inicio, end=" 👉 ")
    b = inicio + segundo
    inicio = segundo
    segundo = b
    qtd -= 1
