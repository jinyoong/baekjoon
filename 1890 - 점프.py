N = int(input())

numbers = [list(map(int, input().split())) for _ in range(N)]
done = [[0] * N for _ in range(N)]
done[0][0] = 1
dr = [0, 1]
dc = [1, 0]


def solution():
    for r in range(N):
        for c in range(N):
            if not done[r][c]:
                continue

            step = numbers[r][c]
            if not step:  # 현재 위치에서 갈 수 있는 거리가 0 이면 넘어감
                continue

            for i in range(2):
                nr, nc = r + step * dr[i], c + step * dc[i]

                if nr >= N or nc >= N:
                    continue

                done[nr][nc] += done[r][c]
                # 만약 [r, c] 위치까지 갈 수 있는 방법이 2가지 였다면
                # 자연스럽게 [nr, nc] 까지 갈 수 있는 방법은 왼쪽, 오른쪽 당 2개씩 증가한다

    return done[N - 1][N - 1]


print(solution())


# queue = [(0, 0)]
# head = 0
# rear = 1
# answer = 0
#
# while head < rear:
#     r, c = queue[head]
#     step = numbers[r][c]
#     head += 1
#
#     if step == 0:
#         continue
#
#     for i in range(2):
#         nr, nc = r + step * dr[i], c + step * dc[i]
#
#         if (nr, nc) == (N - 1, N - 1):
#             answer += 1
#             continue
#
#         if nr >= N or nc >= N:
#             continue
#
#         queue.append((nr, nc))
#         rear += 1
#
# print(answer)

"""
9
3 1 2 2 3 3 1 1 2
1 1 2 1 1 2 3 1 2
2 1 1 3 2 2 1 3 1
3 3 1 1 1 3 1 2 1
3 2 2 2 1 1 3 3 1
3 1 3 2 2 3 1 3 3
3 1 1 2 1 1 1 1 1
2 3 1 3 1 3 2 2 2
3 3 3 2 3 1 3 3 0

4
1 2 2 3
1 1 3 3
3 1 1 3
3 2 1 0
"""
