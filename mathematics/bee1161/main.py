def calculate(number):
    if number < 0:
        return "Fatorial não existe para negativos"

    factorial = 1

    for i in range(1, number + 1):
        factorial *= i

    return factorial


while True:
    try:
        m, n = map(int, input().split())

        print(calculate(n) + calculate(m))

    except EOFError:
        break
