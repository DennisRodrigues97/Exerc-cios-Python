# Escreva um programa que leia o salário de um funcionário e calcule o seu aumento.
# Para salários superiores a R$ 1250,00, calcular um aumento de 10%.
# Para salários inferiores ou iguais o aumento é de 15%.

print("Aumento de salário")

salario = float(input("Salário: "))

if salario > 1250:
    aumento = (salario * 10 / 100) + salario
    print("Salário com aumento: R${:.2f}".format(aumento))
else:
    aumento = (salario * 15 / 100) + salario
    print("Salário com aumento: R${:.2f}".format(aumento))
