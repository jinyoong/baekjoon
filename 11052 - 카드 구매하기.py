N = int(input())

numbers = [0] + list(map(int, input().split()))


def solution(n, cards):
    """
    지금 사야하는 카드의 개수가 n 개라면, n 개까지의 가격을 개당 가격으로 바꿔서 가장 비싼 걸 n // 가격 만큼 산다
    """
    answer = 0

    while n > 0:
        max_cost = 0
        idx = 0

        for i in range(1, n+1):
            cost = cards[i] / i
            if cost > max_cost:
                max_cost = cost
                idx = i

        cnt = n // idx
        n %= idx
        answer += cards[idx] * cnt

    return answer


def solution_dp(n, cards):
    answer = [cards[1]] * (n + 1)

    for i in range(2, n+1):
        max_value = cards[i]
        start = i - 1
        finish = start // 2
        for j in range(start, finish - 1, -1):
            if answer[j] + answer[i-j] > max_value:
                max_value = answer[j] + answer[i-j]
        answer[i] = max_value

    return answer[-1]


print(solution(N, numbers))
print(solution_dp(N, numbers))
