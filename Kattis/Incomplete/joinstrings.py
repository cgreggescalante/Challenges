# Join Strings

N = int(input())

strings = {i: input() for i in range(N)}
# print(strings)
for _ in range(N-1):
    a, b = map(int, input().split())

    strings[a-1] += strings.pop(b-1)

print(list(strings.values())[0])
