n = int(input())

paper = [list(map(int, input().split())) for i in range(n)]
white = blue = 0

dr = [0, 0, 1, 1]
dc = [0, 1, 0, 1]


def cut_paper(paper):
    global white, blue
    t = len(paper)

    if paper == [[1] * t] * t:
        blue += 1
        return

    if paper == [[0] * t] * t:
        white += 1
        return

    mid = len(paper) // 2
    for i in range(4):  # 현재 종이를 4등분 했을 때 선택할 구역
        temp = [[0] * mid for _ in range(mid)]  # 새로운 종이
        for j in range(mid):
            new_row = dr[i]*mid+j
            for k in range(mid):
                new_col = dc[i]*mid+k
                temp[j][k] = paper[new_row][new_col]
        cut_paper(temp)


cut_paper(paper)

print(white)
print(blue)
