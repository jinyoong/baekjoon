import sys

custom_input = sys.stdin.readline

N = int(custom_input())
lst = [list(map(int, custom_input().split())) for _ in range(N)]


def solution(paper):
    answer = 0

    board = [[0] * 101 for _ in range(101)]

    for paper_element in paper:
        x, y = paper_element

        for r in range(10):
            for c in range(10):

                if board[x + r][y + c]:
                    continue

                board[x + r][y + c] = 1
                answer += 1

    return answer


print(solution(lst))
