def quick_sort(list1):
    if len(list1) <1:
        return list1
    middle_num = list1[len(list1)//2]
    left_list = [x for x in list1 if x<middle_num]
    middle_list = [x for x in list1 if x==middle_num]
    right_list = [x for x in list1 if x>middle_num]
    return quick_sort(left_list) + middle_list + quick_sort(right_list)

result = quick_sort([0.577, 1.414, 1.618, 1.732, 2.718, 3.14])
print(result)