# Spavanac

H, M = map(int, input().split())

M -= 45

if M >= 0:
    print(H, M)
else:
    H = (H - 1) % 24
    M += 60
    print(H, M)
