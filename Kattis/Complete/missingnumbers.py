# Missing Numbers

n = int(input())

missed = False
previous = 0
for _ in range(n):
    x = int(input())
    for i in range(previous + 1, x):
        print(i)
        missed = True
    previous = x

if not missed:
    print("good job")
