T = int(input())

num_lst = list(map(int, input().split()))
num_lst_2 = list(set(num_lst))
num_lst_2.sort()

num_dict = {}

for i in range(len(num_lst_2)):
    num_dict[num_lst_2[i]] = i

for i in range(len(num_lst)-1):
    print(num_dict[num_lst[i]], end = " ")
print(num_dict[num_lst[-1]])