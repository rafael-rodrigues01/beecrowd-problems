import sys

raw_data = sys.stdin.read().splitlines()

it = iter(raw_data)

n = int(next(it))

for i in range(n):

    pair_of_strings = next(it).split()

    list_of_caracters1, list_of_caracters2 = map(list, pair_of_strings)

    length = len(list_of_caracters1)

    if len(list_of_caracters1) < len(list_of_caracters2):
        length = len(list_of_caracters2)

    result = ""

    for i in range(length):

        if list_of_caracters1:

            result += list_of_caracters1.pop(0)

        if list_of_caracters2:
            result += list_of_caracters2.pop(0)

    print(result)
