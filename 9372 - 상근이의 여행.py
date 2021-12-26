import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    lst = [map(int, input().split()) for _ in range(M)]
    print(N-1)

'''
def dfs(num, cnt):
    global answer, result, stop

    if 0 not in result[1:]:
        if cnt < answer:
            answer = cnt
            stop = True
        return

    if stop:
        return

    for i in adj_lst[num]:
        if (num, i) in visited:
            continue
        visited.add((num, i))
        result[i] += 1

        if not (i, num) in visited:
            cnt += 1

        dfs(i, cnt)

        if stop:
            return

        if not (i, num) in visited:
            cnt -= 1

        visited.remove((num, i))
        result[i] -= 1


T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    adj_lst = [[] for _ in range(N+1)]
    for _ in range(K):
        v, w = map(int, input().split())
        adj_lst[v].append(w)
        adj_lst[w].append(v)

    answer = N * 2
    visited = set()
    stop = False
    result = [0] * (N + 1)
    result[1] = 1
    dfs(1, 0)

    print(answer)
'''
