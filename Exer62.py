primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
contador = 10
cont_termos = 0

while contador > 0:
    print(primeiro_termo, end=" ")
    print(' 👉 ' if contador != 1 else ' ✅ ', end="")
    primeiro_termo = primeiro_termo + razao
    contador -= 1
    cont_termos += 1
    if contador == 0:
        mais_termos = int(input("\nQuantos termos a mais você quer exibir? "))
        contador = mais_termos

print(f'\n{cont_termos} termos foram exibidos')

