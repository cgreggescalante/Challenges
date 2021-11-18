# Delimiter Soup

n = int(input())

line = input()

stack = []
pairs = {"(": ")", "{": "}", "[": "]"}

for i in range(n):
    if line[i] == " ":
        continue
    if line[i] in "({[":
        stack.append(line[i])
    elif len(stack) > 0 and pairs[stack[-1]] == line[i]:
        stack = stack[:-1]
    else:
        print(line[i], i)
        quit()

if i == n - 1:
    print("ok so far")
