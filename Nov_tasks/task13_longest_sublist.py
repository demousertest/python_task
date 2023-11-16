# nums = [4, 3, 6, 16, 8, 2]
# sorted_list = sorted(nums)
# result = []
# for i in range(len(sorted_list)):
#     for j in range(i, len(sorted_list)):
#         if sorted_list[i]**2 == sorted_list[j] and sorted_list[i] not in result:
#             result.append(sorted_list[i])
#             result.append(sorted_list[j])
#         elif sorted_list[i]**2 == sorted_list[j] and sorted_list[j] not in result:
#             result.append(sorted_list[j])

# if len(result) > 0:
#     print(len(result))
# else:
#     print(-1)


from itertools import combinations
nums = [4, 3, 6, 16, 8, 2]
n = len(nums)
result = []
len_como = 0
for r in range(1, n + 1):
    for combo in combinations(nums, r):
        combo = list(sorted(combo))
        if len(combo)>1:
            test = []
            for i in range(len(combo)):
                for j in range(2, len(combo)):
                    if pow(combo[i],j) in combo or combo[i] == combo[-1]:
                        test.append(True)
                    else:
                        test.append(False)
            if all(test):
                if len(combo)>len_como:

                    len_como = len(combo)
                    result = combo

if len(result) > 0:
    print(f"length of max streak is {len(result)} and result is {result}")
else:
    print(-1)
