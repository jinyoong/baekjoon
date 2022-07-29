n = int(input())


def solution(number):
    visited = [0] * (number + 1)
    visited[number] = 1
    queue = [[number]]
    idx = 0
    length = 1

    while idx < length:
        lst = queue[idx]
        num = lst[-1]
        idx += 1

        if num == 1:
            print(len(lst) - 1)
            print(*lst)
            break

        for i in range(3):
            new_num = 0

            if i == 0 and not num % 3:
                new_num = num // 3

            if i == 1 and not num % 2:
                new_num = num // 2

            if i == 2:
                new_num = num - 1

            if new_num and not visited[new_num]:
                visited[new_num] = 1
                queue.append(lst + [new_num])
                length += 1


solution(n)
