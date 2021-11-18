# Bus Numbers

N = int(input())

nums = sorted(list(map(int, input().split())))

while nums:
    if len(nums) < 3:
        print(' '.join(map(str, nums)))
        break
    start = nums.pop(0)
    i = 0
    while i < len(nums) and nums[i] - i - 1 == start:
        i += 1
    if i > 1:
        print(f"{start}-{nums[i-1]}", end=" ")
        nums = nums[i:]
    else:
        print(start, end=" ")
