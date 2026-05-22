from collections import deque

while True:
    n = int(input())

    if n == 0:
        break

    wagons_a = deque(input().split())
    expected = deque(input().split())

    station = []
    result = []

    while expected:

        if station and station[-1] == expected[0]:
            station.pop()
            expected.popleft()
            result.append("R")

        elif wagons_a:
            station.append(wagons_a.popleft())
            result.append("I")

        else:
            result.append(" Impossible")
            break

    print("".join(result))
