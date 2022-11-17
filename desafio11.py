
#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input("Digite largura: "))
altura = float(input("Digite altura: "))
area = largura * altura
qtd_tinta = area / 2
print("Você precisa de {:.2f}l. de tinta para pintar {:.2f}m².".format(qtd_tinta, area))
