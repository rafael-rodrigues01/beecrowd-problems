notas = [100, 50, 20, 10, 5, 2, 1]
valor_inicial = int(input())
print(valor_inicial)

valor_restante = valor_inicial

# Em vez de while True + i += 1, use:
for nota in notas:
    quantidade = valor_restante // nota
    valor_restante %= nota  # O resto vira o novo valor para a próxima nota
    print(f"{quantidade} nota(s) de R$ {nota},00")
