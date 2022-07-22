numbers = [list(map(int, input().split())) for _ in range(5)]
answer = 0
check = set()
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(stack):
    global answer

    if not stack:
        return

    r, c, number = stack[-1]
    stack.pop(-1)

    if len(number) == 6:
        if number not in check:
            answer += 1
            check.add(number)
        return

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]

        if nr < 0 or nr >= 5 or nc < 0 or nc >= 5:
            continue

        new_number = number + str(numbers[nr][nc])
        dfs(stack + [(nr, nc, new_number)])


for sr in range(5):
    for sc in range(5):
        dfs([(sr, sc, str(numbers[sr][sc]))])

print(answer)
