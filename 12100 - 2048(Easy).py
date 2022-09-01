N = int(input())

game = [list(map(int, input().split())) for _ in range(N)]
answer = 0


def solution(board, n, count):
    global answer

    if count == 5:
        result = 0
        for board_ele in board:
            if result < max(board_ele):
                result = max(board_ele)

        if answer < result:
            answer = result
        return

    for new_direction in range(4):
        new_board = [[0] * n for _ in range(n)]
        can_merge = True

        if new_direction == 0:  # 왼쪽으로 이동시키는 경우
            for r in range(n):
                idx = -1
                for c in range(n):

                    if not board[r][c]:
                        continue

                    if new_board[r][idx] == board[r][c] and can_merge:
                        new_board[r][idx] *= 2
                        can_merge = False

                    else:
                        idx += 1
                        can_merge = True
                        new_board[r][idx] = board[r][c]

        elif new_direction == 1:  # 오른쪽으로 이동시키는 경우
            for r in range(n):
                idx = 0
                for c in range(n - 1, -1, -1):

                    if not board[r][c]:
                        continue

                    if new_board[r][idx] == board[r][c] and can_merge:
                        new_board[r][idx] *= 2
                        can_merge = False

                    else:
                        idx -= 1
                        can_merge = True
                        new_board[r][idx] = board[r][c]

        elif new_direction == 2:  # 위로 이동시키는 경우
            for c in range(n):
                idx = -1
                for r in range(n):

                    if not board[r][c]:
                        continue

                    if new_board[idx][c] == board[r][c] and can_merge:
                        new_board[idx][c] *= 2
                        can_merge = False

                    else:
                        idx += 1
                        can_merge = True
                        new_board[idx][c] = board[r][c]

        else:  # 아래로 이동시키는 경우
            for c in range(n):
                idx = 0
                for r in range(n - 1, -1, -1):

                    if not board[r][c]:
                        continue

                    if new_board[idx][c] == board[r][c] and can_merge:
                        new_board[idx][c] *= 2
                        can_merge = False

                    else:
                        idx -= 1
                        can_merge = True
                        new_board[idx][c] = board[r][c]

        solution(new_board, n, count + 1)


solution(game, N, 0)
print(answer)


"""
문제점 찾은 반례
5
2 2 4 4 8
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
왼쪽으로 이동시키면

4 8 8 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
이렇게 되야 하는데

4 4 4 8 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
이 된다

=> 39, 61, 83, 105 줄에 can_merge = True 를 넣어줬다
=> 합쳐진 수 다음에 위치하는 숫자는 합쳐질 수 있으니까 True 로 바꿔줘야 한다

"""
