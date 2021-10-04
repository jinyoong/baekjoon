import sys

sys.stdin = open('3184.txt')


def solution(field, n, m):
    total_s = total_w = 0  # 최종적으로 남은 양과 늑대의 수
    visited = [[0] * m for _ in range(n)]  # 방문 표시를 하기 위한 리스트
    location = []  # 양 또는 늑대가 위치한 좌표
    for i in range(n):
        for j in range(m):
            if field[i][j] == 'v' or field[i][j] == 'o':
                location.append([i, j])

    # 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    def move(loc, s_cnt, w_cnt):  # 현재 좌표에서부터 시작
        queue = [loc]
        while queue:
            r, c = queue.pop(0)
            visited[r][c] = 1
            for i in range(4):
                new_r = r + dr[i]
                new_c = c + dc[i]
                if new_r < 0 or new_r >= n or new_c < 0 or new_c >= m:  # 범위를 벗어나면 패스
                    continue
                if field[new_r][new_c] == '#':  # 울타리면 패스
                    continue
                temp = field[new_r][new_c]
                if visited[new_r][new_c]:  # 한 번 방문했던 좌표면 패스
                    continue
                if temp == 'v':  # 늑대면 늑대의 수 1 증가
                    w_cnt += 1
                elif temp == 'o':  # 양이면 양의 수 1 증가
                    s_cnt += 1
                queue.append([new_r, new_c])  # 다음 좌표 추가
                visited[new_r][new_c] = 1  # 방문처리

        if w_cnt >= s_cnt:  # 늑대의 수가 양의 수 이상이면 다 먹는다
            return 0, w_cnt
        else:  # 양의 수가 더 많으면 늑대는 쫓겨난다
            return s_cnt, 0

    for loc in location:
        if not visited[loc[0]][loc[1]]:
            if field[loc[0]][loc[1]] == 'v':  # 현재 좌표가 늑대면
                temp = move(loc, 0, 1)  # 늑대는 1마리부터 시작
            else:
                temp = move(loc, 1, 0)  # 양은 1마리부터 시작
            total_s += temp[0]
            total_w += temp[1]

    return total_s, total_w


n, m = map(int, input().split())
field = [list(input()) for _ in range(n)]
print(*solution(field, n, m))
