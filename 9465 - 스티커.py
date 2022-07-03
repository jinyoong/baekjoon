T = int(input())

for _ in range(T):
    n = int(input())
    stickers = [list(map(int, input().split())) + [0] for _ in range(2)]
    # temp = [[[0, 0] for _ in range(n)] for _ in range(2)]
    # temp[0][0][0] = stickers[0][0]
    # temp[1][0][0] = stickers[1][0]
    # temp[1][0][1] = stickers[0][0]
    #
    # for c in range(1, n):
    #     for r in range(2):
    #         temp[r][c][0] = stickers[r][c] +
    #         max(temp[r][c - 1][1], temp[(r + 1) % 2][c][1], temp[(r + 1) % 2][c - 1][0])
    #         temp[r][c][1] = max(max(temp[r][c - 1]), max(temp[(r + 1) % 2][c]))
    #
    # print(max(temp[1][n - 1]))
    for i in range(1, n):
        # 대각선 방향의 i - 1 번째와, i - 2 번째 중 큰 값을 더하는 과정은
        # i - 1 번째 스티커를 뜯는게 좋을지, i - 2 번째 스티커를 뜯는게 좋을지 판단하는 과정이랑 같다
        stickers[0][i] += max(stickers[1][i - 1], stickers[1][i - 2])
        stickers[1][i] += max(stickers[0][i - 1], stickers[0][i - 2])

    print(max(stickers[0][n - 1], stickers[1][n - 1]))
