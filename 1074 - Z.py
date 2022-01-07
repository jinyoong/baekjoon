"""
def draw_z(n, r, c, target):
    global cnt
    global stop
    if n == 1:
        for ele in [[0, 0], [0, 1], [1, 0], [1, 1]]:
            nr = r + ele[0]
            nc = c + ele[1]
            if [nr, nc] == target:
                stop = True
                return
            cnt += 1
    else:
        for ele in [[0, 0], [0, 1], [1, 0], [1, 1]]:
            weight = 2**(n-1)
            start_row = r + ele[0] * weight
            start_col = c + ele[1] * weight
            draw_z(n-1, start_row, start_col, target)
            if stop:
                return


n, r, c = map(int, input().split())
cnt = 0
stop = False
draw_z(n, 0, 0, [r, c])
print(cnt)
"""


def find_num(n, r, c, cnt, target_r, target_c):
    if n == 1:
        for i in range(4):
            nr = r + locations[i][0]
            nc = c + locations[i][1]
            if target_r != nr or target_c != nc:
                continue
            return cnt + i

    weight = 2 ** (n-1)
    isright = 1
    isdown = 1
    if target_r < r + weight:
        isright = 0

    if target_c < c + weight:
        isdown = 0

    qudrant = [isright, isdown]
    plus = weight ** 2 * locations.index(qudrant)
    nr = r + qudrant[0] * weight
    nc = c + qudrant[1] * weight
    return find_num(n-1, nr, nc, cnt+plus, target_r, target_c)


n, r, c = map(int, input().split())
locations = [[0, 0], [0, 1], [1, 0], [1, 1]]
print(find_num(n, 0, 0, 0, r, c))
