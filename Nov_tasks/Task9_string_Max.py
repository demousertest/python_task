words = ["This", "is", "an", "example", "of", "text", "justification."]
result, test_list, num_of_letter = [], [], 0
maxWidth = 16
for word in words:
    if len(word) + len(test_list) + num_of_letter >maxWidth:
        for i in range(maxWidth - num_of_letter):
            test_list[i % (len(test_list) - 1 or 1)] += ' '
        result.append("".join(test_list))
        test_list, num_of_letter = [],0
                
    test_list += [word]
    num_of_letter += len(word)
result.append(" ".join(test_list).ljust(maxWidth))
# print(result)

for i in result:
    print(i)