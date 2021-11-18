# Shopaholic

n = int(input())

nums = sorted(map(int, input().split()))[::-1]
s = sum([nums[i] for i in range(2, len(nums), 3)])
print(s)
