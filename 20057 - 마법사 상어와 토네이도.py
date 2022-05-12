def solution(n):
    result = 0
    sr = sc = n // 2
    idx = 0
    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]

    while True:
        check[sr][sc] = 1
        temp_idx = (idx + 1) % 4
        nr, nc = sr + dr[idx], sc + dc[idx]
        tr, tc = nr + dr[temp_idx], nc + dc[temp_idx]
        sand = remain = numbers[nr][nc]
        numbers[nr][nc] = 0

        if idx % 2 == 0:
            t1 = [sr + dr[(idx + 1) % 4], sc, 1]
            t2 = [sr + dr[(idx + 3) % 4], sc, 1]
            t3 = [sr + dr[(idx + 1) % 4], sc + dc[idx], 7]
            t4 = [sr + dr[(idx + 3) % 4], sc + dc[idx], 7]
            t5 = [sr + dr[(idx + 1) % 4], sc + 2 * dc[idx], 10]
            t6 = [sr + dr[(idx + 3) % 4], sc + 2 * dc[idx], 10]
            t7 = [sr + 2 * dr[(idx + 1) % 4], sc + dc[idx], 2]
            t8 = [sr + 2 * dr[(idx + 3) % 4], sc + dc[idx], 2]
            t9 = [sr, sc + 3 * dc[idx], 5]
            t10 = [sr, sc + 2 * dc[idx], 100]
        else:
            t1 = [sr, sc + dc[(idx + 1) % 4], 1]
            t2 = [sr, sc + dc[(idx + 3) % 4], 1]
            t3 = [sr + dr[idx], sc + dc[(idx + 1) % 4], 7]
            t4 = [sr + dr[idx], sc + dc[(idx + 3) % 4], 7]
            t5 = [sr + 2 * dr[idx], sc + dc[(idx + 1) % 4], 10]
            t6 = [sr + 2 * dr[idx], sc + dc[(idx + 3) % 4], 10]
            t7 = [sr + dr[idx], sc + 2 * dc[(idx + 1) % 4], 2]
            t8 = [sr + dr[idx], sc + 2 * dc[(idx + 3) % 4], 2]
            t9 = [sr + 3 * dr[idx], sc, 5]
            t10 = [sr + 2 * dr[idx], sc, 100]

        for ele in [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]:
            fr, fc, rt = ele
            fly_result = fly(fr, fc, sand, rt)

            if ele == t10:
                fly_result[1] = remain

            if fly_result[0] == "out":
                result += fly_result[1]
            else:
                numbers[fr][fc] += fly_result[1]
            remain -= fly_result[1]

        if not check[tr][tc]:
            idx = (idx + 1) % 4

        if [nr, nc] == [0, -1]:
            return result + remain * 2
        else:
            sr, sc = nr, nc


def fly(x, y, before, ratio):
    result = (before * ratio) // 100
    if x < 0 or x >= N or y < 0 or y >= N:
        return ["out", result]
    else:
        return ["in", result]


N = int(input())

numbers = [list(map(int, input().split())) for _ in range(N)]
check = [[0] * N for _ in range(N)]

print(solution(N))
