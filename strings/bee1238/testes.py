strs = ["rafa", "ren"]
n = 2

string1 = list(strs[0])
string2 = list(strs[1])

length = len(string1)

if len(string1) < len(string2):
    length = len(string2)

print("tamanho:", length)

result = ""

for i in range(length):

    if string1:

        result += string1.pop(0)

    if string2:
        result += string2.pop(0)

print(result)
