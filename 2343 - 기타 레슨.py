N, M = map(int, input().split())
lectures = list(map(int, input().split()))
start = max(lectures)
end = sum(lectures)
answer = 987654321

while start <= end:

    middle = (start + end) // 2
    selected = [0] * N
    idx = 0

    for k in range(M):
        result = 0
        for i in range(idx, N):
            if result + lectures[i] > middle:
                idx = i
                break

            result += lectures[i]
            selected[i] = 1

    if 0 not in selected:
        if answer > middle:
            answer = middle
        end = middle - 1
    else:
        start = middle + 1

print(answer)
