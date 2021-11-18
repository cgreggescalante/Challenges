# Even Up Solitaire

n = int(input())

cards = [i % 2 for i in map(int, input().split())]


while True:
    i = 0
    prev = len(cards)
    labels = [1 for _ in range(prev)]
    while i < len(cards) - 1:
        if cards[i] == cards[i+1]:
            labels[i] = 0
            labels[i+1] = 0
            n -= 2
            i += 2
        else:
            i += 1
    cards = [cards[i] for i in range(len(cards)) if labels[i]]
    if prev == len(cards):
        break

print(n)
