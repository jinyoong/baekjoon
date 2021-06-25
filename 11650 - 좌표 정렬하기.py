T = int(input())

num_list = []

for i in range(T):
    a, b = map(int, input().split())
    num_list.append([a,b])

num_list = sorted(num_list, key=lambda x:(x[0], x[1]))

for i in range(T):
    print(num_list[i][0], num_list[i][1])