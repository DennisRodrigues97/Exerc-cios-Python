from datetime import date

ano = int(input("Ano de nascimento: "))
a = date.today().year

idade = a - ano

if idade > 18:
    print("Já passaram {} anos do tempo de alistamento.".format(idade - 18))
elif idade < 18:
    print("Ainda vai se alistar, faltam {} anos para alistamento.".format(18 - idade))
else:
    print("Está na hora de se alistar.")

