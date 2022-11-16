
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considerando o dólar à R$ 3,27.

dinheiro = float(input("Diga quanto tem BRL R$: "))
print("Você poderia comprar USD $: {:.2f} com BRL R$ {}".format(dinheiro/3.27, dinheiro))
