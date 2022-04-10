import sys


def solution(sr, sc, n):
    """
    sr : 종이에서 살펴볼 시작 행
    sc : 종이에서 살펴볼 시작 열
    n : 종이의 크기
    """
    global answer
    first = numbers[sr][sc]
    is_cut = False

    for i in range(n):
        nr = sr + i
        for j in range(n):
            nc = sc + j
            current = numbers[nr][nc]
            if first != current:
                is_cut = True
                break
        if is_cut:
            break

    if not is_cut:
        answer[first + 1] += 1
        return

    # 다른 숫자가 포함되어 있는 경우
    for i in range(3):
        for j in range(3):
            solution(sr + (n // 3) * i, sc + (n // 3) * j, n // 3)


N = int(input())

numbers = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = [0, 0, 0]
solution(0, 0, N)

for ans in answer:
    print(ans)
