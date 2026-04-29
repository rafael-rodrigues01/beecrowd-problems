notas = [100, 50, 20, 10, 5, 2, 1]

n = int(input())
print(n)

i = 0

while True:
    divisor_atual = notas[i]
    quociente = n // divisor_atual
    resto = n % divisor_atual

    print(f"{quociente} nota(s) de R$ {notas[i]},00")

    n = resto
    i += 1

    if i == len(notas):
        break
