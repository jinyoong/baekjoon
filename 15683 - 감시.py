N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
answer = 987654321
cctv = {1: [(0, 1)],
        2: [(0, -1), (0, 1)],
        3: [(-1, 0), (0, 1)],
        4: [(0, -1), (-1, 0), (0, 1)],
        5: [(0, -1), (-1, 0), (0, 1), (1, 0)]}


def rotate():
    result_dict = {}

    for number in range(1, 6):
        result = []

        for i in range(4):
            temp = []
            if number == 2 and i >= 2:
                continue

            elif number == 5 and i >= 1:
                continue

            for ele in cctv[number]:
                new_ele = (-ele[1], ele[0])
                temp.append(new_ele)

            cctv[number] = temp
            result.append(cctv[number])

        result_dict[number] = result

    return result_dict


cctv_dict = rotate()


def find_cctv():
    result = []
    count = 0

    for r in range(N):
        for c in range(M):
            count += 1

            if 1 <= office[r][c] <= 5:
                result.append((r, c))
                count -= 1

            if office[r][c] == 6:
                count -= 1

    return [result, count]


def solution(new_office, idx, result, total):
    global answer

    if idx == len(cctv_lst):
        if answer > total - result:
            answer = total - result
        return

    temp_office = [new_office[r][:] for r in range(N)]

    for i in range(idx, len(cctv_lst)):

        r, c = cctv_lst[i]
        direction = cctv_dict[office[r][c]]

        for j in range(len(direction) + 1):

            if j == len(direction):
                return

            # print("{}, {} 의 값은 {} 이고 가능한 방향은 {}".format(r, c, office[r][c], direction[j]))
            count = 0
            for d in direction[j]:

                nr, nc = r, c
                while True:

                    if nr < 0 or nr >= N or nc < 0 or nc >= M:
                        break

                    if temp_office[nr][nc] == 6:
                        break

                    count += 1
                    if temp_office[nr][nc]:
                        count -= 1
                    else:
                        temp_office[nr][nc] = -1

                    nr += d[0]
                    nc += d[1]

            solution(temp_office, idx + 1, result + count, total)
            temp_office = [new_office[r][:] for r in range(N)]


cctv_lst, total = find_cctv()
solution(office, 0, 0, total)
print(answer)
