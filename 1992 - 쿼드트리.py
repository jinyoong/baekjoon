def solution(sr, sc, n):
    global answer

    is_stop = False
    start = numbers[sr][sc]
    for r in range(n):
        for c in range(n):
            current = numbers[sr + r][sc + c]
            if start != current:
                is_stop = True
                break
        if is_stop:
            break

    if not is_stop:
        answer += str(start)
    else:
        answer += "("

        for k in range(4):
            nr, nc = sr + pr[k] * (n // 2), sc + pc[k] * (n // 2)
            solution(nr, nc, n // 2)

        answer += ")"
    return


N = int(input())

numbers = [[] for _ in range(N)]
answer = ""
pr = [0, 0, 1, 1]
pc = [0, 1, 0, 1]

for i in range(N):
    numbers[i] = list(map(int, input()))

solution(0, 0, N)
print(answer)
