"""
지름길의 도착 위치가 고속도로의 길이 D 보다 큰 경우 볼 필요 없음
지름길의 실제 거리(도착 위치 - 시작 위치)가 지름길의 길이보다 짧은 경우 볼 필요 없음
어차피 주어지는 지름길은 최대 12개니까 재귀로 완전탐색 해보자
"""
N, D= map(int, input().split())

shortcuts = []
for _ in range(N):
    start, finish, length = map(int, input().split())
    if finish > D:
        continue
    if finish - start < length:
        continue
    shortcuts.append([start, finish, length])

start = 0
answer = D
shortcuts = sorted(shortcuts, key=lambda x: x[0])


def minimum(start, result):
    global answer
    for shortcut in shortcuts:
        if shortcut[0] < start:  # 시작위치가 지금 위치보다 앞인 경우 패스
            continue
        if shortcut[0] == start:  # 시작위치가 현재 위치랑 같은 경우 일단 지름길 써보기
            minimum(shortcut[1], result+shortcut[2])
        if shortcut[0] > start:  # 지금 보고 있는 시작위치가 현재 위치보다 뒤에 있으면 시작위치까지 이동해서 지름길 써보기
            move = shortcut[0] - start
            minimum(shortcut[1], result+shortcut[2]+move)

    if D - start + result < answer:
        answer = D - start + result

    return


minimum(0, 0)

print(answer)
