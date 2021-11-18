# Mortal Fibonacci Rabbits

n = 81
m = 16

rabbits = [1]

while n > 1:
    total = sum(rabbits[1:])
    rabbits = [total] + rabbits
    if len(rabbits) > m:
        rabbits = rabbits[:m]
    n -= 1

print(sum(rabbits))
