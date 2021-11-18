# Final Exam

n = int(input())

prev = input()

score = 0

for _ in range(n-1):
    c = input()
    score += prev == c
    prev = c

print(score)
