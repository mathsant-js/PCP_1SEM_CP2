print("===== CÁLCULO DA MÉDIA ===== ")
print(" - A seguir, informe suas notas relaciondas aos Checkpoints (0 a 10): ")
cp1 = float(input("Digite sua nota do Checkpoint 1: "))
if cp1 > 10:
    print("Nota inválida! Tente novamente...")
    exit()

cp2 = float(input("Digite sua nota do Checkpoint 2: "))
if cp2 > 10:
    print("Nota inválida! Tente novamente...")
    exit()

cp3 = float(input("Digite sua nota do Checkpoint 3: "))
if cp3 > 10:
    print("Nota inválida! Tente novamente...")
    exit()

print(" - Agora, informe suas notas relacionadas aos Sprint e ao Global Solution (0 a 10): ")

sp1 = float(input("Digite sua nota do Sprint 1: "))
if sp1 > 10:
    print("Nota inválida! Tente novamente...")
    exit()

sp2 = float(input("Digite sua nota do Sprint 2: "))
if sp2 > 10:
    print("Nota inválida! Tente novamente...")
    exit()

gs = float(input("Digite sua nota do Global Solution: "))
if gs > 10:
    print("Nota inválida! Tente novamente...")
    exit()

if cp1 <= cp2 and cp1 <= cp3:
    cp1 = 0
elif cp2 <= cp1 and cp2 <= cp3:
    cp2 = 0
else:
    cp3 = 0

soma_cps = cp1 + cp2 + cp3
media = ((soma_cps + sp1 + sp2 ) / 4) * 0.4 + (gs * 0.6)

mediaPeso = media * 0.4

print(f"- A média do semestre (sem peso): {media:.1f}")
print(f"- A média do semestre com peso: {mediaPeso:.1f}")