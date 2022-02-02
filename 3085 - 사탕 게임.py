import sys

input = sys.stdin.readline


def bomboni(r, c):

    garo_max = 1
    sero_max = 1
    for i in range(N):
        garo_cnt = 1
        sero_cnt = 1
        for j in range(1, N):
            if candy_box[i][j-1] == candy_box[i][j]:
                garo_cnt += 1
            else:
                if garo_max < garo_cnt:
                    garo_max = garo_cnt
                garo_cnt = 1

            if candy_box[j-1][i] == candy_box[j][i]:
                sero_cnt += 1
            else:
                if sero_max < sero_cnt:
                    sero_max = sero_cnt
                sero_cnt = 1

        if garo_max < garo_cnt:
            garo_max = garo_cnt

        if sero_max < sero_cnt:
            sero_max = sero_cnt

        if garo_max == N or sero_max == N:
            return N

    return max(garo_max, sero_max)


def solution():
    answer = 0

    for r in range(N):
        for c in range(N-1):
            if r <= N-2:
                candy_box[r][c], candy_box[r + 1][c] = candy_box[r + 1][c], candy_box[r][c]
                if bomboni(r, c) > answer:
                    answer = bomboni(r, c)
                candy_box[r][c], candy_box[r + 1][c] = candy_box[r + 1][c], candy_box[r][c]

            candy_box[r][c], candy_box[r][c + 1] = candy_box[r][c + 1], candy_box[r][c]
            if bomboni(r, c) > answer:
                answer = bomboni(r, c)
            candy_box[r][c], candy_box[r][c + 1] = candy_box[r][c + 1], candy_box[r][c]

            if answer == N:
                return answer

    return answer


N = int(input())

candy_box = [[] for _ in range(N)]
for i in range(N):
    candy_box[i] = list(input())

print(solution())
