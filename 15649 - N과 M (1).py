N, K = map(int, input().split())

# 1~N까지를 K개 택하는 문제
# idx + 1, cnt

sel = [0] * K # 선택한 k개를 담을 변수

def solution(idx, cnt):
    if cnt == K:
        print(*sel)
        return

    if idx == N:
        return

    for i in range(idx, N+1):
        sel[cnt] = i
        solution(i, cnt+1)

solution(0, 0)