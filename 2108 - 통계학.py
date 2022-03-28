N = int(input())

num_list = [0] * N
num_dict = {}
num_sum = 0
max_num = -4000
min_num = 4000

for i in range(N):
    temp = int(input())
    if max_num < temp:
        max_num = temp
    if min_num > temp:
        min_num = temp
    num_sum += temp
    num_list[i] = temp
    num_dict[temp] = num_dict.get(temp, 0) + 1

many_value = 0
many_key = []
for key, value in num_dict.items():
    if value > many_value:
        many_value = value
        many_key = [key]
        continue

    if value == many_value:
        many_key.append(key)

many_key.sort()

num_list.sort()
print(round(num_sum / N))
print(num_list[N//2])
print(many_key[1] if len(many_key) >= 2 else many_key[0])
print(max_num - min_num)
