'''
must be even
ends in zero
multiple of 20
'''

nums = [3, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19]
for i in range(20, 10000000000000, 20):
    works = True
    for x in nums:
        if not i % x == 0:
            works = False
    if works:
        print(i)
