# dica do chat é usar variáveis pythonicas: snake_case

peso_a = 3.5
peso_b = 7.5

nota_a = float(input())
nota_b = float(input())

media_ponderada = (nota_a * peso_a + nota_b * peso_b) / (peso_b + peso_b)

print(f"MEDIA = {media_ponderada:.5f}")
