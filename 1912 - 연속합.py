def solution(n):
    lst = [0] * n
    lst[0] = numbers[0]

    for i in range(1, n):
        temp = lst[i - 1] + numbers[i]

        if temp <= numbers[i]:
            lst[i] = numbers[i]
        else:
            lst[i] = temp

    return max(lst)


N = int(input())

numbers = list(map(int, input().split()))

print(solution(N))
