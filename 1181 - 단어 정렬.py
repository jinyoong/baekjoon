T = int(input())

str_lst = []

for i in range(T):
    s = input()
    if s not in str_lst:
        str_lst.append(s)


str_lst = sorted(str_lst, key=lambda x:(len(x), x))

for i in range(len(str_lst)):
    print(str_lst[i])