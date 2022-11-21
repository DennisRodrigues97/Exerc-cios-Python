print("Shampoo R$18,99")

preco = 18.99
a_vista = preco - (10 / 100) * preco
a_vista_cartao = preco - (5 / 100) * preco
parcelado3x = preco + (20 / 100) * preco

print("Qual a forma de pagamento?\n")
tipo_pagamento = int(input("1 - DINHEIRO\n2 - CHEQUE\n3 - CARTÃO\n"))

if tipo_pagamento == 1 or tipo_pagamento == 2:
    preco = a_vista
elif tipo_pagamento == 3:
    forma_pagamento = int(input("1 - À VISTA\n2 - PARCELADO\n"))
    if forma_pagamento == 2:
        parcela = int(input("Número de parcelas: "))
        if parcela >= 3:
            preco = parcelado3x
        else:
            preco = a_vista_cartao
    else:
        preco = a_vista_cartao

print("Valor à pagar R${:.2f}".format(preco))