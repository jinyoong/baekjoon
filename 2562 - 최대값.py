num_list = []

for i in range(9):
    num_list.append(int(input()))

max_num = 0

for i in range(9):
    if max_num <= num_list[i]:
        max_num = num_list[i]

print(max_num)
print(num_list.index(max_num) + 1)