def ehNegativo(numero):
    return numero < 0

def ehZero(numero):
    return numero == 0

def ehString(texto):
    if any(char.isdigit() for char in texto) or texto == "":
        return False
    return True

def erroNome(nome):
    if not ehString(nome):
        print("\n[ERRO]: O nome não pode ser vazio ou um número")

def erroIdade(idade):
    if ehNegativo(idade):
        print("\n[ERRO]: A idade não pode ser negativa!")
    elif ehZero(idade):
        print("\n[ERRO]: A idade não pode ser 0!")

def erroFloat(valor):
    if ehNegativo(valor):
        print("\n[ERRO]: O número não pode ser negativo")
    elif ehZero(valor):
        print("\n[ERRO]: O número não pode ser 0!")

def erroParcela(parcela):
    if ehNegativo(parcela):
        print("\n[ERRO]: O número de parcelas não deve ser negativo!")
    elif ehZero(parcela):
        print("\n[ERRO]: O número de parcelas não pode 0!")

while True:
    nome = input("\nDigite o seu nome...\n")
    erroNome(nome)
    if ehString(nome):
        break

while True:
    idade = int(input("\nDigite a sua idade...\n"))
    erroIdade(idade)
    if not ehZero(idade) and not ehNegativo(idade):
        break

while True:
    renda = float(input("\nDigite a sua renda mensal...\n"))
    erroFloat(renda)
    if not ehZero(renda) and not ehNegativo(renda):
        break

while True:
    valor = float(input("\nDigite o valor desejado do empréstimo...\n"))
    erroFloat(valor)
    if not ehZero(valor) and not ehNegativo(valor):
        break

while True:
    parcelas = int(input("\nDigite o número de parcelas...\n"))
    erroParcela(parcelas)
    if not ehZero(parcelas) and not ehNegativo(parcelas):
        break


def pode_aprovar(idade, renda, valor):
    return idade > 17 and valor <= renda * 20

def definir_taxa(parcelas):
    if parcelas < 7:
        return 0.05
    elif parcelas < 13:
        return 0.08
    else:
        return 0.1

def calcular_parcela(valor, taxa, parcelas):
    return valor * (taxa * (1 + taxa) ** parcelas) / ((1 + taxa) ** parcelas - 1)

def calcular_total(parcela, parcelas):
    return parcela * parcelas

def calcular_juros(total, valor):
    return total - valor

def exibir_info(nome, valor, taxa_percentual, valor_parcela, valor_total, valor_juros):
    print("\n==== INFORMAÇÕES DO EMPRÉSTIMO ====")
    print(f"Nome do cliente: {nome}")
    print(f"Valor financiado: R${valor:.2f}")
    print(f"Taxa de juros: {taxa_percentual:.0f}%")
    print(f"Valor da parcela: R${valor_parcela:.2f}")
    print(f"Valor total pago: R${valor_total:.2f}")
    print(f"Total de juros pago: R${valor_juros:.2f}")


if not(pode_aprovar(idade, renda, valor)):
    print("\nEmpréstimo negado: idade mínima não atingida ou valor excede 20x a renda!")
elif parcelas > 24:
    print("\nEmpréstimo negado: O número máximo de parcelas é 24!\n")
else:
    taxa_juros = definir_taxa(parcelas)
    valor_parcela = calcular_parcela(valor, taxa_juros, parcelas)
    valor_total = calcular_total(valor_parcela, parcelas)
    valor_juros = calcular_juros(valor_total, valor)

    taxa_percentual = taxa_juros * 100
    exibir_info(nome, valor, taxa_percentual, valor_parcela, valor_total, valor_juros)