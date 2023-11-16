from itertools import combinations
nums = [2, 1, 4]
n = len(nums)
result = 0
for r in range(1, n + 1):
    for combo in combinations(nums, r):
        print(combo)
        total = (max(combo) **2 * min(combo))%(10**9+7)
        result += total
print(result)