result = []

N = int(input())
numbers = list(map(int, input().split()))
operator_cnt = list(map(int, input().split()))
operator = ['+', '-', '*', '/']


def calculator(idx, fin):
    if idx == N:
        result.append(fin)
        return

    for i in range(4):
        if operator_cnt[i] != 0:  # 현재 위치에 사용할 연산자가 남아있으면
            operator_cnt[i] -= 1  # 사용할 개수를 1개 줄인다
            if i == 0:  # 더하기
                temp = fin + numbers[idx]
            elif i == 1:  # 뺴기
                temp = fin - numbers[idx]
            elif i == 2:  # 곱하기
                temp = fin * numbers[idx]
            else:  # 나누기
                if fin >= 0:
                    temp = fin // numbers[idx]
                else:  # 0보다 작으면 규칙대로 하자
                    temp = -(-fin // numbers[idx])
            calculator(idx+1, temp)
            operator_cnt[i] += 1
    return


calculator(1, numbers[0])

print(max(result))
print(min(result))
