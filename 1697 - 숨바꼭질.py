n, k = map(int, input().split())

check = [-1] * 200000
check[n] = 0
queue = [n]
head = 0

while True:
    loc = queue[head]
    head += 1

    if loc == k:
        print(check[loc])
        break

    for i in range(3):
        temp = 0
        if i == 0:
            temp = loc - 1

        elif i == 1:
            temp = loc + 1

        else:
            temp = loc * 2

        if temp >= 200000:
            continue

        if check[temp] != -1:
            continue

        if temp < 0:
            continue

        queue.append(temp)
        check[temp] = check[loc] + 1
