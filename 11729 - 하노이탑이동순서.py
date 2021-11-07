# 처음 1이 이동하는 부분은 3, 2 가 번갈아서 이동하게 된다
# 즉, 홀수 개인 경우 1은 3부터 가고 짝수 개인 경우 1은 2부터 간다

location = [1, 0, 0]
# 놓을 위치보다 옮기는 숫자가 더 작은 경우에만 이동이 가능


def solution(location, start):
    for i in range(3):
        if i == start:
            continue
        if location[i][-1] > location[start][-1]:
            change_num = location[start].pop()
            location[i].append(change_num)
            answer.append((start, i))
            start = i
            solution(location, start)

    return


n = int(input())

answer = []
if n % 2:
    location = [[i for i in range(n, 1, -1)], [], [1]]
else:
    location = [[i for i in range(n, 1, -1)], [1], []]

if n == 1:
    print(1)
    print(1, 3)

print(solution(location, 0))
