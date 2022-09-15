N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


def solution(road_map, slope, n):
    answer = 0

    for r in range(n):
        before = road_map[r][0]
        down_clear = True
        length = 1

        for c in range(1, n):
            current = road_map[r][c]

            if abs(before - current) > 1:
                break

            if current == before:
                length += 1

                if not down_clear and length == slope:
                    down_clear = True
                    length = 0

            elif current > before:  # 오른쪽이 더 높은 경우
                if not down_clear:
                    break

                if length >= slope:
                    length = 1
                else:
                    break

            else:  # 오른쪽이 더 낮은 경우
                if not down_clear:
                    break

                length = 1
                down_clear = False

                if slope == 1:
                    down_clear = True
                    length = 0

            before = current

        else:
            if not down_clear:
                continue

            answer += 1

    for c in range(n):
        before = road_map[0][c]
        down_clear = True
        length = 1

        for r in range(1, n):
            current = road_map[r][c]

            if abs(before - current) > 1:
                break

            if current == before:
                length += 1

                if not down_clear and length == slope:
                    down_clear = True
                    length = 0

            elif current > before:  # 아래쪽이 더 높은 경우
                if not down_clear:
                    break

                if length >= slope:
                    length = 1
                else:
                    break

            else:  # 아래쪽이 더 낮은 경우
                if not down_clear:
                    break

                length = 1
                down_clear = False

                if slope == 1:
                    down_clear = True
                    length = 0

            before = current

        else:
            if not down_clear:
                continue

            answer += 1

    return answer


print(solution(board, L, N))
