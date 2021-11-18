# Guess the Number

low = 0
high = 1001

while True:
    mid = (low + high) // 2
    print(mid)
    response = input()
    if response == "lower":
        high = mid
    elif response == "higher":
        low = mid
    else:
        break
