N, M = map(int, input().split())
numbers = [list(map(int, input().split())) for _ in range(N)]


def solution(board, n, m):
    answer = 987654321
    chicken = []
    house_count = 0

    for r in range(n):
        for c in range(n):
            if board[r][c] == 2:
                chicken.append((r, c))

            if board[r][c] == 1:
                house_count += 1

    lines = [[0] * len(chicken) for _ in range(house_count)]
    idx = 0

    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:

                for i in range(len(chicken)):
                    house_line = abs(r - chicken[i][0]) + abs(c - chicken[i][1])
                    lines[idx][i] = house_line

                idx += 1

    permutation_lst = []

    def permutation(start, length, maximum, result):

        if len(result) == maximum:
            permutation_lst.append(result)
            return

        for number in range(start, length):
            permutation(number + 1, length, maximum, result + [number])

    permutation(0, len(chicken), m, [])

    for permutation_ele in permutation_lst:
        ele_result = 0
        for line in lines:
            chicken_line = 987654321

            for ele_idx in permutation_ele:

                if line[ele_idx] < chicken_line:
                    chicken_line = line[ele_idx]

            ele_result += chicken_line

        if ele_result < answer:
            answer = ele_result

    return answer


print(solution(numbers, N, M))
