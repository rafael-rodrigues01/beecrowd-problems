import math

n = int(input())

for i in range(n):
    deck1, deck2 = input().split()

    mdc = math.gcd(int(deck1), int(deck2))
    print(mdc)
