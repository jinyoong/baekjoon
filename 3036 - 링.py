T = int(input())

num_list = list(map(int, input().split()))

for i in range(1, T):
    if num_list[0] <= num_list[i]:
        min = num_list[0]
        max = num_list[i]
    else:
        min = num_list[i]
        max = num_list[0]
    while min :
        max, min = min, max % min
    print('{}/{}'.format(num_list[0]//max, num_list[i]//max))