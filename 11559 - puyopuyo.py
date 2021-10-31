def puyo_pop(point, alpha):

    queue = [point]
    head = 0
    rear = 1  # 큐의 길이 => 같은 뿌요의 수

    while head < rear:

        r, c = queue[head]
        head += 1

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= 12 or nc < 0 or nc >= 6:
                continue

            if [nr, nc] in queue:
                continue

            if puyo[nr][nc] == alpha:
                queue.append([nr, nc])
                rear += 1

    if rear < 4:
        return 0

    for ele in queue:
        r, c = ele
        puyo[r][c] = '.'

    return 1


def puyo_new():  # 아래에서부터 쌓아주기
    for j in range(6):
        for i in range(11, -1, -1):
            if puyo[i][j] == '.':  # .을 만나면
                idx = i
                while idx >= 0 and puyo[idx][j] == '.':  # 행을 한 칸 씩 위로 올라가면서 .이 아닌 경우를 찾자
                    idx -= 1
                if idx < 0:  # 행의 맨 꼭대기까지 도달하면 멈춤
                    break
                puyo[i][j], puyo[idx][j] = puyo[idx][j], puyo[i][j]


def solution():
    global answer
    is_change = 0

    for i in range(12):
        for j in range(6):
            if puyo[i][j] == '.':
                continue
            is_change += puyo_pop([i, j], puyo[i][j])  # 1번 이상 터지는지 확인하기 위한 방법

    if is_change:
        puyo_new()
        answer += 1
        solution()


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
puyo = [list(input()) for _ in range(12)]
answer = 0
solution()
print(answer)
