T = int(input())

lst = []
num_lst = []

for i in range(T):
    age, name = input().split()
    lst.append([int(age), name])
    num_lst.append(int(age))

lst = sorted(lst, key=lambda x:x[0])

for i in range(T):
    print(lst[i][0], lst[i][1])