start = int(input())

check = set()
queue = [[start, 0]]
head = 0
rear = 1

while head < rear:
    number, cnt = queue[head]
    head += 1

    if number == 1:
        print(cnt)
        break

    if number in check:
        continue

    check.add(number)

    if number % 3 == 0:
        queue.append([number // 3, cnt + 1])
        rear += 1

    if number % 2 == 0:
        queue.append([number // 2, cnt + 1])
        rear += 1

    queue.append([number - 1, cnt + 1])
    rear += 1
