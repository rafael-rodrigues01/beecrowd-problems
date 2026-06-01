# versão usando math.factorial

import math

while True:
    try:
        m, n = map(int, input().split())
        print(math.factorial(m) + math.factorial(n))

    except EOFError:
        break

# Versão manual melhorada:


def factorial(number):
    result = 1

    for i in range(2, number + 1):
        result *= i

    return result


while True:
    try:
        m, n = map(int, input().split())

        print(factorial(m) + factorial(n))

    except EOFError:
        break
