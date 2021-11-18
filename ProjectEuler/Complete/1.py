# Multiples of 3 and 5

print(
    sum(
        {i for i in range(5, 1000, 5)}
            .union({i for i in range(3, 1000, 3)})
    )
)
