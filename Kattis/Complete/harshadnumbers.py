# Harshad Numbers

n = int(input())

while True:
    sd = sum(map(int, str(n)))
    if n % sd == 0:
        print(n)
        break
    n += 1
