# Digits of Pi
# ID: 270
# Key: PIVAL

def pi_generate():
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    while True:
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = (10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x)
        else:
            q, r, t, k, m, x = (q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2)


n = 8400
digits = pi_generate()

# build a list of characters, the leading 3 and n decimals
pi_list = []
for i in range(n+1):
    pi_list.append(str(next(digits)))

pi_list.insert(1, '.')

pi_str = "".join(pi_list)

print(pi_str)
