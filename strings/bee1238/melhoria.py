n = int(input())

for _ in range(n):
    s1, s2 = input().split()

    result = ""

    for i in range(max(len(s1), len(s2))):

        if i < len(s1):
            result += s1[i]

        if i < len(s2):
            result += s2[i]

    print(result)
