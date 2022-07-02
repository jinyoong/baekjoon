N = int(input())

if N == 1:
    print("*")

else:
    w, h = 5 + 4 * (N - 2), 7 + 4 * (N - 2)
    width, height = w, h
    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]
    r, c = 0, width - 1
    idx = 0
    stars = [[" "] * width for _ in range(height)]

    while width > 0:

        if idx % 2:
            for _ in range(height - 1):
                stars[r][c] = "*"
                nr, nc = r + dr[idx % 4], c + dc[idx % 4]
                if nr < 0 or nr >= h or nc < 0 or nc >= w:
                    continue
                r, c = nr, nc
            idx += 1
            height -= 2

        else:
            for _ in range(width - 1):
                stars[r][c] = "*"
                nr, nc = r + dr[idx % 4], c + dc[idx % 4]
                if nr < 0 or nr >= h or nc < 0 or nc >= w:
                    continue
                r, c = nr, nc
            idx += 1
            if idx != 1:
                width -= 2

    stars[r][c] = "*"

    for i in range(h):
        answer = "".join(stars[i])
        if i == 1:
            print("*")
        else:
            print(answer)
