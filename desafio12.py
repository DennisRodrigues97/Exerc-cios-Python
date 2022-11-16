#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Diga o preço: "))
desconto = preco * (5/100)
print("O preço com desconto é R$: {:.2f}".format(preco - desconto))
