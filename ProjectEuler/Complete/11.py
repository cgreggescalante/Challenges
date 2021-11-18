grid = []

file = open('Resources/Grid11.txt', 'r').readlines()

for line in file:
        nums = [int(a) for a in line.split()]
        grid.append(nums)


products = []

def up(x, y):
        prod = 1
        for i in range(0, 4):
                prod *= grid[x - i][y]
        products.append(prod)


def down(x, y):
        prod = 1
        for i in range(0, 4):
                prod *= grid[x + i][y]
        products.append(prod)


def left(x, y):
        prod = 1
        for i in range(0, 4):
                prod *= grid[x][y - i]
        products.append(prod)


def right(x, y):
        prod = 1
        for i in range(0, 4):
                prod *= grid[x][y + i]
        products.append(prod)


def diagUL(x, y):
        prod = 1
        for i in range(0, 4):
                prod *= grid[x - i][y - i]
        products.append(prod)


def diagUR(x, y):
        prod = 1
        for i in range(0, 4):
                prod *= grid[x - i][y + i]
        products.append(prod)


def diagDL(x, y):
        prod = 1
        for i in range(0, 4):
                prod *= grid[x + i][y - i]
        products.append(prod)


def diagDR(x, y):
        prod = 1
        for i in range(0, 4):
                prod *= grid[x + i][y + i]
        products.append(prod)



for x in range(20):
        for y in range(20):
                if x > 2:
                        up(x, y)
                if x < 17:
                        down(x, y)
                if y > 2:
                        left(x, y)
                if y < 17:
                        right(x, y)
                if x > 2 and y > 2:
                        diagUL(x, y)
                if x > 2 and y < 17:
                        diagUR(x, y)
                if x < 17 and y > 2:
                        diagDL(x, y)
                if x < 17 and y < 17:
                        diagDR(x, y)

print(max(products))
