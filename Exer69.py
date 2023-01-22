mais18 = 0
homens = 0
mulheresMenos20 = 0

while True:
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [F ou M]: ")).upper().strip()
    continuar = str(input("Continuar? [S ou N]: ")).upper().strip()

    if idade > 18:
        mais18 += 1
    if sexo in 'M':
        homens += 1
    if idade < 20 and sexo in 'F':
        mulheresMenos20 += 1
    if continuar == 'N':
        break
    while continuar != "S":
        continuar = str(input("Continuar? [S ou N]: ")).upper().strip()

print(f'Pessoas com mais de 18 anos: {mais18}')
print(f'Homens cadastrados: {homens}')
print(f'Mulheres com menos de 20 anos: {mulheresMenos20}')
