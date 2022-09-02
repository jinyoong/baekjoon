N, M = map(int, input().split())
numbers = [list(input()) for _ in range(M)]


def solution(soldiers, w, h):
    result = [0, 0]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for r in range(h):
        for c in range(w):

            if not soldiers[r][c]:
                continue

            standard = soldiers[r][c]
            queue = [(r, c)]
            idx = 0
            length = 1
            soldiers[r][c] = ""

            while idx < length:
                cr, cc = queue[idx]
                idx += 1

                for i in range(4):
                    nr, nc = cr + dr[i], cc + dc[i]

                    if nr < 0 or nr >= h or nc < 0 or nc >= w:
                        continue

                    if not soldiers[nr][nc]:
                        continue

                    adj_soldier = soldiers[nr][nc]

                    if adj_soldier != standard:
                        continue

                    queue.append((nr, nc))
                    soldiers[nr][nc] = ""
                    length += 1

            if standard == "W":
                result[0] += length ** 2
            else:
                result[1] += length ** 2

    return result


print(*solution(numbers, N, M))
