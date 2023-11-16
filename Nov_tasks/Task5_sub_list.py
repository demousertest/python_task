list1 = [1,2,3,4,5,6,7]
k = 2
out_put =[]
for i in range(len(list1)):
    sort_list = []
    if len(list1) >= k:
        for _ in range(k):
            sort_list.append(list1.pop(0))
    out_put = out_put +sorted(sort_list,reverse=True)

if list1 :
    out_put =out_put+list1

print(out_put)