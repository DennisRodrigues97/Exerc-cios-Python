from datetime import date

sexo = str(input("Digite F para femenino ou M para masculino: ")).lower()
print(sexo)
a = date.today().year

if sexo == "f":
    print("Mulheres não precisam se alista!")
elif sexo == "m":
    ano = int(input("Ano de nascimento: "))
    idade = a - ano
    ano_alistamento = ano + 18
    if idade > 18:
        print("Você tem {} anos.\nJá passaram {} anos do tempo de alistamento.\nSeu alistamento foi em {}.".format(idade, idade - 18, ano_alistamento))
    elif idade < 18:
        print("Você tem {} anos.\nAinda vai se alistar.\nFaltam {} anos para alistamento.".format(idade, 18 - idade, ano_alistamento))
    else:
        print("Você tem {} anos.\nEstá na hora de se alistar.".format(idade))
else:
    print("Opção inválida!")

