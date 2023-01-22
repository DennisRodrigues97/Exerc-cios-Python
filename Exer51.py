primeiro_termo = int(input("Primeiro termo PA: "))
razao = int(input("Razão da PA: "))
num = primeiro_termo

print(f'{"Os dez primeiros termos dessa progressão são: ":~^100}')
print(primeiro_termo, end=" ")
for a in range(primeiro_termo, primeiro_termo+9):
    num = num + razao
    print(">", num, end=" ")
print("> Acabou", end="")
