def calcular_preco_por_kg(codigo_carga):
    if 10 <= codigo_carga <= 20:
        return 100
    elif 21 <= codigo_carga <= 30:
        return 250
    elif 31 <= codigo_carga <= 40:
        return 340
    else:
        return 0

def calcular_imposto(codigo_estado, preco_carga):
    if codigo_estado == 1:
        return preco_carga * 0.35
    elif codigo_estado == 2:
        return preco_carga * 0.25
    elif codigo_estado == 3:
        return preco_carga * 0.15
    elif codigo_estado == 4:
        return preco_carga * 0.05
    elif codigo_estado == 5:
        return 0
    else:
        return 0

# entrada
codigo_estado = int(input("Digite o código do estado de origem (1 a 5): "))
peso_toneladas = float(input("Digite o peso da carga em toneladas: "))
codigo_carga = int(input("Digite o código da carga (10 a 40): "))

# processamento
peso_kg = peso_toneladas * 1000
preco_por_kg = calcular_preco_por_kg(codigo_carga)
preco_carga = peso_kg * preco_por_kg
imposto = calcular_imposto(codigo_estado, preco_carga)
valor_total = preco_carga + imposto

# saída
print(f"\nPeso da carga em kg: {peso_kg:.2f} kg")
print(f"Preço da carga: R$ {preco_carga:.2f}")
print(f"Valor do imposto: R$ {imposto:.2f}")
print(f"Valor total transportado: R$ {valor_total:.2f}")