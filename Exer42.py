r1 = float(input("Primeira reta: "))
r2 = float(input("Segunda reta: "))
r3 = float(input("Terceira reta: "))
maior = float

# confere qual tipo de triângulo poderia ser formado.
tipoTriangulo = str
if r1 == r2 and r2 == r3:
    tipoTriangulo = "equílatero"
elif r1 == r2 or r1 == r3:
    tipoTriangulo = "isóceles"
elif r1 != r2 and r2 != r3:
    tipoTriangulo = "escaleno"

# Calcula qual o maior lado
if r1 > r2 and r1 > r3:
    maior = r1
elif r2 > r3:
    maior = r2
else:
    maior = r3

# Outra opção para validar se é possível formar um triângulo
# if r1 + r2 > r3 and r2 + r3 > r1 and r2 + r1 > r3:
#     print("Pode formar triângulo.")
# else:
#     print("Não pode formar triângulo.")

# Calcula se a soma de todos os lados menos o lado maior, para identificar se pode ser formado triângulo.
triangulo = r1 + r2 + r3 - maior

# valida se a variavel anterior é maior que o maior lado, se sim executa o bloco verdadeiro.
if triangulo > maior:
    print("Estas retas podem formar um triângulo do tipo {}.".format(tipoTriangulo))
else:
    print("Estas retas não podem formar um triângulo!")


