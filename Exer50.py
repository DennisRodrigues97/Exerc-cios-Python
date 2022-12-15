soma = 0
cont = 0
for n in range(0, 6):
    nums = int(input("{}º número: ".format(n+1)))
    if nums % 2 == 0:
        soma += nums
        cont += 1
if cont > 1:
    print("A soma dos {} números pares é {}.".format(cont, soma))
elif cont == 1:
    print("Você digitou apenas 1 número par, o número {}.".format(soma))
elif cont == 0:
    print("Você não digitou nenhum número par.")
    