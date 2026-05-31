options = ["A", "B", "C", "D", "E"]

while True:
    n = int(input())

    if n == 0:
        break

    for answers in range(n):
        int_answers = [int(x) for x in input().split()]

        dict_answers = dict(zip(options, int_answers))

        result = {}

        for name, value in dict_answers.items():
            if value <= 127:
                result[name] = "Preenchido"

        if not result:
            print("*")
        elif len(result) > 1:
            print("*")
        else:
            print(next(iter(result)))
