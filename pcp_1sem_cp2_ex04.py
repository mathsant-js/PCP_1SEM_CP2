def calcular_horas_extras(sb, horas):
    return sb * 0.015 * horas

def calcular_descontos_faltas(sb, falta):
    return sb * 0.02 * falta

def calcular_bonus(cargo, bonus):
    if not bonus:
        return 0
    bonus_por_cargo = {1: 1000, 2: 500, 3: 300, 4: 100}
    return bonus_por_cargo.get(cargo, 0)

nome = input("Digite seu nome: ")

print ("Cargos: 1 - Gerente, 2 - Analista, 3 - Assistente, 4 - Estagiário")
cargo = int(input("Selecione seu cargo: "))

sb = float(input("Digite seu salário bruto: R$"))
horas_extras = float(input("Digite a quantidade de horas extras: "))
falta = int(input("Digite a quantidade de faltas: "))
bonus = input("Você tem direito a bônus? (s/n): ")
rb = bonus == "s"

valor_horas_extras = calcular_horas_extras(sb, horas_extras)
valor_bonus = calcular_bonus(cargo, rb)
total_acrescimos   = valor_horas_extras + valor_bonus

total_descontos    = calcular_descontos_faltas(sb, falta)

salario_bruto      = sb + total_acrescimos
salario_final      = salario_bruto - total_descontos

cargos = {1: "Gerente", 2: "Analista", 3: "Assistente", 4: "Estagiário"}

print(f"\n{'='*40}")
print(f"  Holerite - {nome} ({cargos.get(cargo, 'Desconhecido')})")
print(f"{'='*40}")
print(f"  Salário base:        R$ {sb:>10.2f}")
print(f"  Horas extras:        R$ {valor_horas_extras:>10.2f}")
print(f"  Bônus:               R$ {valor_bonus:>10.2f}")
print(f"  Total de acréscimos: R$ {total_acrescimos:>10.2f}")
print(f"  Total de descontos:  R$ {total_descontos:>10.2f}")
print(f"{'='*40}")
print(f"  Salário final:       R$ {salario_final:>10.2f}")
print(f"{'='*40}")
