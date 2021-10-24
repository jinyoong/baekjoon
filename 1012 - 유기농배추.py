def solution(locations):

    answer = 0

    # 상, 우, 하, 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    visited = [0] * K

    for i in range(K):
        if visited[i]:
            continue

        queue = [[] for _ in range(K)]
        head = 0
        rear = 1
        queue[0] = locations[i]
        visited[i] = 1
        answer += 1

        while head < rear:

            row, col = queue[head]
            head += 1

            for i in range(4):
                new_row = row + dr[i]
                new_col = col + dc[i]

                new_p = [new_row, new_col]

                for i in range(K):
                    if locations[i] == new_p and not visited[i]:
                        visited[i] = 1
                        queue[rear] = new_p
                        rear += 1
                        break

    return answer


T = int(input())

for test_case in range(1, T+1):
    M, N, K = map(int, input().split())
    locations = [list(map(int, input().split())) for _ in range(K)]
    print(solution(locations))
