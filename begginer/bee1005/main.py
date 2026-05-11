pesoA = 3.5
pesoB = 7.5

notaA = float(input())
notaB = float(input())

media_ponderada = (notaA * pesoA + notaB * pesoB) / (pesoA + pesoB)

print(f"MEDIA = {media_ponderada:.5f}")
