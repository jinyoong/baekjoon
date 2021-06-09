T = int(input())

num_list = []

for i in range(T):
    num_list.append(int(input()))

start_index = 0

while start_index < T:
    for i in range(1, T):
        if num_list[i - 1] > num_list[i]:
            num_list[i - 1], num_list[i] = num_list[i], num_list[i - 1]
    start_index += 1

for i in range(T):
    print(num_list[i])