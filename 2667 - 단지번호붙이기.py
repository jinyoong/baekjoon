def complex_cnt(apt, r, c):
    result = 1
    apt[r][c] = 0
    queue = [tuple() for _ in range(25*25)]
    queue[0] = (r, c)
    head = 0
    rear = 1

    while head < rear:
        r, c = queue[head]
        head += 1

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if not apt[nr][nc]:
                continue

            apt[nr][nc] = 0
            queue[rear] = (nr, nc)
            rear += 1
            result += 1

    return result


def solution(apt, n):
    ans_cnt = 0
    ans_lst = []

    for i in range(n):
        for j in range(n):
            if not apt[i][j]:
                continue
            ans_cnt += 1
            ans_lst.append(complex_cnt(apt, i, j))

    return ans_cnt, ans_lst


N = int(input())

apt = [[] for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(N):
    temp = list(map(int, input()))
    apt[i] = temp

cnt, lst = solution(apt, N)
print(cnt)
lst.sort()
for ele in lst:
    print(ele)
