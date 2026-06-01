options = ["A", "B", "C", "D", "E"]

while True:
    n = int(input())

    if n == 0:
        break

    for _ in range(n):
        values = list(map(int, input().split()))

        marked = [option for option, value in zip(options, values) if value <= 127]

        print(marked[0] if len(marked) == 1 else "*")
