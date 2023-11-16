nums = [1, -1, -3, -2, 3]
k = 3
x = 2
result = []
def get_beatuy(sublist):
    neg_num = sorted([i for i in sublist if i<=0])
    return neg_num[x-1] if len(neg_num)>=x else 0

for i in range(len(nums)-k+1):
    sublists = nums[i:i+k]
    result.append(get_beatuy(sublists))
print(result)   