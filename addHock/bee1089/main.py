import sys
import os

input_path = "addHock/bee1089/input.txt"
file_exists = os.path.exists(input_path)

if file_exists:
    sys.stdin = open(input_path, "r")


raw_data = sys.stdin.read().splitlines()

it = iter(raw_data)
pico = 0
i = 0

for line in it:
    n = int(line)
    if n == 0:
        break

    notas = [int(x) for x in next(it).split()]

    for current_item in notas:
        length = len(notas)

        if (
            current_item > notas[i - 1]
            and current_item > notas[(i + 1) % length]
            or current_item < notas[i - 1]
            and current_item < notas[(i + 1) % length]
        ):

            pico += 1

        i += 1

    i = 0
    print(pico)
    pico = 0
