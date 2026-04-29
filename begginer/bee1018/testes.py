notas = [100, 50, 20, 10, 5, 2, 1]

# n = int(input())

n = 11257

results = {
    "count_100_bill": 0,
    "count_50_bill": 0,
    "count_20_bill": 0,
    "count_10_bill": 0,
    "count_5_bill": 0,
    "count_2_bill": 0,
    "count_1_bill": 0,
}

i = 0

while True:
    divisor_atual = notas[i]
    quociente = n // divisor_atual
    resto = n % divisor_atual

    if divisor_atual == 100:
        results["count_100_bill"] = quociente
    elif divisor_atual == 50:
        results["count_50_bill"] = quociente
    elif divisor_atual == 20:
        results["count_20_bill"] = quociente
    elif divisor_atual == 10:
        results["count_10_bill"] = quociente
    elif divisor_atual == 5:
        results["count_5_bill"] = quociente
    elif divisor_atual == 2:
        results["count_2_bill"] = quociente
    elif divisor_atual == 1:
        results["count_1_bill"] = quociente

    n = resto
    i += 1

    if n == 0:
        break

i = 0

for k, v in results.items():
    print(f"{v} nota(s) de R$ {notas[i]},00")
    i += 1
