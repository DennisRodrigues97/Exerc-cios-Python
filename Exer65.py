decisao = str # 'S'
soma = maior = menor = cont = 0

#while decisao in 'Ss':
while decisao != "N":
    numeros = int(input("Números: "))
    decisao = str(input("Continuar ?\n(S) ou (N): ")).strip().upper()#[0]
    soma += numeros
    if cont == 0:
        maior = menor = numeros
    else:
        if numeros > maior:
            maior = numeros
        if numeros < menor:
            menor = numeros
    cont += 1
print(f'\nMédia: {soma/cont:.2f}\nMaior: {maior}\nMenor: {menor}')
