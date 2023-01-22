"""
fatorial = 5
for i in range(1, fatorial):
    fatorial = fatorial * i
    print(fatorial)
"""


fatorial = int(input("Número fatorial: "))
num = fatorial
contador = 1

while contador != num:
    fatorial = fatorial * contador
    contador += 1

print(f"Fatorial de {num}! = ", end="")

while num >= 1:
    print(f"{num}", end="")
    print(" = " if num == 1 else " x ", end="")
    num -= 1
print(f"{fatorial}")
