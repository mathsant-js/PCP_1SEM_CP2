# funcoes
def ordenar_lados(a, b, c):
    # ordenando em decrescente: A,B,C
    if b > a:
        a, b = b, a
    if c > a:
        a, c = c, a
    if c > b:
        b, c = c, b
    return a, b, c

def classificar_triangulo(A, B, C):
    if A >= B + C:
        return "NAO FORMA TRIANGULO"
    
    if A**2 == B**2 + C**2:
        return "TRIANGULO RETANGULO"
    elif A**2 > B**2 + C**2:
        return "TRIANGULO OBTUSANGULO"
    else:
        return "TRIANGULO ACUTANGULO"

def classificar_lados(A, B, C):
    if A == B and B == C:
        return "TRIANGULO EQUILATERO"
    elif A == B or A == C or B == C:
        return "TRIANGULO ISOSCELES"
    else:
        return ""

# entrada, processamento, saida
a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

A, B, C = ordenar_lados(a, b, c)
tipo_triangulo = classificar_triangulo(A, B, C)
tipo_lados = classificar_lados(A, B, C)


print(f"\nLados em ordem decrescente: {A}, {B}, {C}")
print(tipo_triangulo)

if tipo_triangulo != "NAO FORMA TRIANGULO" and tipo_lados != "":
    print(tipo_lados)