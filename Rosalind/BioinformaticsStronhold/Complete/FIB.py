# Rabbits and Recurrence Relations

n = 31
k = 4
t = 1

two = 0
one = 0

while n > 0:
    t += one
    one = two
    two = t * k
    n -= 1

print(t)