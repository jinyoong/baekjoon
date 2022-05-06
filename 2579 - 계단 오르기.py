N = int(input())

stairs = [0] + [int(input()) for _ in range(N)]

numbers = [[0] * 3 for i in range(N + 1)]
# 맨 처음 지점은 계단으로 취급하지 않기 때문에 1칸 + 1칸 식으로 올라갈 수 있다
# 그래서 첫 번째 계단을 다 밟았다고 해놓고 시작해야 한다
numbers[1] = [stairs[1]] * 3


for i in range(2, N + 1):
    """
    1칸+2칸
    2칸+1칸
    2칸+2칸
    이렇게 3가지 경우로 나눠서 생각해보자
    """

    # 1칸 + 2칸 상태가 되려면
    # 2칸 전이 2칸 + 1칸 이어야 한다
    numbers[i][0] = stairs[i] + numbers[i-2][1]

    # 2칸 + 1칸 상태가 되려면
    # 이전 칸까지 1칸 + 2칸, 2칸 + 2칸 이어야 한다
    numbers[i][1] = stairs[i] + max(numbers[i-1][0], numbers[i-1][2])

    # 2칸 + 2칸 상태가 되려면
    # 2칸 전이 1칸 + 2칸, 2칸 + 2칸 이어야 한다
    numbers[i][2] = stairs[i] + max(numbers[i-2][0], numbers[i-2][2])

print(max(numbers[N]))
