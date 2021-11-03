import sys


def solution(n, m, lst):
    answer = 1  # 비가 n 보다 적은 양이 온 경우는 안전한 영역은 1개

    for i in range(n, m):  # n 이상 m 미만으로 비가 오는 경우
        temp = [[0] * N for _ in range(N)]

        for r in range(N):
            for c in range(N):
                if lst[r][c] <= i:  # 현재 온 비보다 낮거나 같은 지역은 0 으로 처리
                    temp[r][c] = 0
                else:
                    temp[r][c] = lst[r][c]

        cnt = 0  # 안전한 영역의 개수를 저장할 변수
        visited = set()  # 방문처리
        for r in range(N):
            for c in range(N):

                if temp[r][c] == 0:  # 지금 보고 있는 땅이 침수된 곳이면 패스
                    continue

                if (r, c) in visited:  # 지금 보고 있는 땅이 한 번 본 땅이면 패스
                    continue

                head = 0
                rear = 1
                queue = [[r, c]]

                while head < rear:
                    cur_r, cur_c = queue[head]
                    head += 1

                    for k in range(4):
                        nr = cur_r + dr[k]
                        nc = cur_c + dc[k]

                        if nr < 0 or nr >= N or nc < 0 or nc >= N:
                            continue

                        if (nr, nc) in visited:
                            continue

                        if temp[nr][nc] == 0:
                            continue

                        queue.append([nr, nc])
                        visited.add((nr, nc))
                        rear += 1

                cnt += 1

        if answer <= cnt:
            answer = cnt

    return answer


N = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
minimum = 100  # 가장 낮은 높이
maximum = 0  # 가장 높은 높이
city = [[] for _ in range(N)]

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    min_num = min(temp)
    max_num = max(temp)
    if minimum > min_num:
        minimum = min_num
    if maximum < max_num:
        maximum = max_num
    city[i] = temp

print(solution(minimum, maximum, city))
