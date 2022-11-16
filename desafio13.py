#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Diga seu salário: R$ "))
aumento = salario * (15/100)
print("Seu salário com aumento de 15% é R$ {:.2f}".format(salario + aumento))
