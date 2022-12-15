from datetime import date
ano = date.today().year
maior = 0
menor = 0
for i in range(0, 7):
    ano_nascimento = int(input("Ano de nascimento {}ª pessoa: ".format(i+1)))
    if ano - ano_nascimento < 18:
        menor += 1
    elif ano - ano_nascimento >= 18:
        maior += 1
print("{} pessoas são maiores de idade e {} são menores.".format(maior, menor))
