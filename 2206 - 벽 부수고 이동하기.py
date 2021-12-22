N, M = map(int, input().split())

result = -1
maps = ['' for _ in range(N)]
answer = [[2] * M for _ in range(N)]
answer[0][0] = 0

for i in range(N):
    maps[i] = input()

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

queue = [[0, 0, 0, 1] for _ in range(10000)]
front = 0
rear = 1

while front != rear:
    r, c, cnt, moving = queue[front]
    front = (front + 1) % 10000

    if r == N-1 and c == M-1:
        result = moving
        break

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue

        if answer[nr][nc] <= cnt:
            continue

        if maps[nr][nc] == '1' and not cnt:
            answer[nr][nc] = 1
            queue[rear] = [nr, nc, cnt+1, moving+1]
            rear = (rear + 1) % 10000

        if maps[nr][nc] == '0':
            answer[nr][nc] = cnt
            queue[rear] = [nr, nc, cnt, moving+1]
            rear = (rear + 1) % 10000

print(result)

'''
8 8
01000100
01010100
01010100
01010100
01010100
01010100
01010100
00010100
답 : 29

5 10
0000011000
1101011010
0000000010
1111111110
1111000000
답 : 14

5 5
01100
01000
01110
01000
00010
답 : 9

8 4
0000
0110
1110
0000
0111
0000
1110
0000
답 : 11

8 8
01000100
01010100
01010100
01010100
01010100
01010100
01010100
00010100
답 : 29
'''