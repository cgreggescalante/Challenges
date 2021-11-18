print(3/7)
# 0.42857142857142855
start = 0
target = 3/7
closest = 1
for d in range(1, 1000001):
    for n in range(start, start + 100):
        if n / d > target:
            if target - ((n-1) / d) < closest and target - ((n-1) / d) > 0:
                closest = target - ((n-1) / d)
                cnum = n-1
                cden = d
                print(str(n-1)+'/'+str(d))
                print((n-1)/d)
                print()
            start = n - 1
            break

print(str(cnum)+'/'+str(cden))
print('Gap :', str(closest))
