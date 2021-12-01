N = int(input())

star_pattern = [[''] * N for _ in range(N)]


def star(r, c, n):
    nr = r + n//3
    nc = c + n//3
    null_size = n//3

    if null_size == 1:
        for i in range(3):
            for j in range(3):
                star_pattern[r+i][c+j] = '*'

        for i in range(null_size):
            for j in range(null_size):
                star_pattern[nr+i][nc+j] = ' '

        return

    for i in range(3):
        for j in range(3):
            star(r + n//3 * i, c + n//3 * j, n//3)

    for i in range(null_size):
        for j in range(null_size):
            star_pattern[nr+i][nc+j] = ' '


star(0, 0, N)
for i in range(N):
    print("".join(star_pattern[i]))
