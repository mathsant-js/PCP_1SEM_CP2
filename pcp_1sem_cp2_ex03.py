print("===== CÁLCULO DA MÉDIA ===== ")
print(" - A seguir, informe suas notas relaciondas aos Checkpoints (0 a 10): ")
cp1 = float(input("Digite sua nota do Checkpoint 1: "))
cp2 = float(input("Digite sua nota do Checkpoint 2: "))
cp3 = float(input("Digite sua nota do Checkpoint 3: "))
print(" - Agora, informe suas notas relacionadas aos Sprint e ao Global Solution (0 a 10): ")
sp1 = float(input("Digite sua nota do Sprint 1: "))
sp2 = float(input("Digite sua nota do Sprint 2: "))
gs = float(input("Digite sua nota do Global Solution: "))

if cp1 < cp2 < cp3 or cp1 < cp3 < cp2:
    cp1 = 0
elif cp2 < cp3 < cp1 or cp2 < cp1 < cp3:
    cp2 = 0
elif cp3 < cp1 < cp2 or cp3 < cp2 < cp1:
    cp3 = 0

media = ((cp1 + cp2 + cp3 + sp1 + sp2 ) / 4) * 0.4 + (gs * 0.6)

mediaPeso = media * 0.4

