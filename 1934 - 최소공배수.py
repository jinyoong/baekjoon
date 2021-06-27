T = int(input())

num_list = []

for i in range(T):
    x, y = map(int, input().split())
    if x < y:
        x, y = y, x
    num_list.append([x, y])

for i in range(T):
    big = num_list[i][0]
    small = num_list[i][1]

    while small:
        big, small = small, big % small

    print(num_list[i][0] * num_list[i][1] // big)