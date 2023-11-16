matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# for i in range(len(matrix)):
#     for j in range(i,len(matrix)):
#         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
# for i in range(len(matrix)):
#     matrix[i] = matrix[i][::-1]
# print(matrix)


output_list = []
for row in zip(*matrix):
    r =list(row)
    for i in range(len(r)):
        for j in range(i,len(r)):
            r[i],r[j] = r[j],r[i]

    output_list.append(r)
print((output_list))