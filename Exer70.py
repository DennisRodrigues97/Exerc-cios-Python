total = mais1000 = menorPreco = contador = 0
produtoMaisBarato  = str
while True:
    nome = str(input("Produto: "))
    preco = float(input("Preço: "))
    continuar = str(input("Continuar? [S ou N]: ")).upper().strip()
    if contador == 1:
        menorPreco = preco
    if preco < menorPreco:
        menorPreco = preco
        produtoMaisBarato = nome
    total += preco
    contador += 1
    if preco > 1000:
        mais1000 += 1
    if continuar == 'N':
        break
    while continuar != 'S':
        continuar = str(input("Continuar? [S ou N]: ")).upper().strip()


print(f'Total: R${total:.2f}')
print(f'Produtos que custam mais de R$1000.00: {mais1000}')
print(f'Produto mais barato: {produtoMaisBarato} R${menorPreco}')

