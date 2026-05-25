from collections import deque
import os, sys

input_path = "dataStructures/bee1063/input.txt"
file_exists = os.path.exists(input_path)

if file_exists:
    sys.stdin = open(input_path, "r")


wagons_b = []


while True:

    station = []
    result = []

    try:
        n_wagons = input().strip()

        if not n_wagons:
            continue

        n_wagons = int(n_wagons)

        if n_wagons == 0:
            break

        wagons_a = deque(input().strip().split())
        expected_wagons = deque(input().strip().split())

        while True:

            if station and station[len(station) - 1] == expected_wagons[0]:
                wagons_b.append(station.pop())
                result.append("R")
                expected_wagons.popleft()

            elif not wagons_a and not station:
                break

            elif not wagons_a and station[len(station) - 1] != expected_wagons[0]:
                result.append(" Impossible")
                break

            else:
                station.append(wagons_a.popleft())
                result.append("I")

        print("".join(result))

    except EOFError:
        break
