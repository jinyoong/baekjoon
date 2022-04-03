def printer_queue(lst, target):
    result = 0
    while True:
        front_value = lst[0]
        print_value = -1
        queue = []
        for idx in range(1, len(lst)):
            if lst[idx][1] > front_value[1]:
                queue += lst[idx:] + [front_value]
                break
            else:
                queue.append(lst[idx])
        else:
            print_value = front_value[0]
            result += 1
        if print_value == target:
            return result
        else:
            lst = queue


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    numbers = list(enumerate(list(map(int, input().split()))))
    print(printer_queue(numbers, M))
