'''
i 번째 기둥 이후의 기둥들 중 가장 큰 기둥의 높이를 봐야 한다
i+1 번째 이후 기둥들 중 i 번째 기둥보다 높은 기둥이 있을 경우, i 번째 기둥의 높이를 유지한 채로 진행
i+1 번째 이후 기둥들 중 i 번째 기둥보다 높은 기둥이 없는 경우, i+1 번째 이후 기둥들 중 가장 높은 높이로 진행
'''
N = int(input())

pillars = [tuple(map(int, input().split())) for _ in range(N)]

pillars = sorted(pillars, key=lambda x: x[0])

answer = 0
w, h = pillars[0]
idx = 0

while idx < N:
    max_h = 0
    max_w = 0
    temp_idx = idx
    for i in range(temp_idx+1, N):
        nw, nh = pillars[i]
        if nh >= h:
            max_h = nh
            max_w = nw
            idx = i
            break

        if nh > max_h:
            max_h = nh
            max_w = nw
            idx = i

    if max_h >= h:
        answer += (max_w - w) * h
    else:
        answer += h + (max_w - w - 1) * max_h
        # i+1 이후의 기둥들 중 제일 높은 기둥이 i 번째 기둥보다 낮은 경우
        # i 번째 기둥의 면적 + 제일 높은 기둥 직전까지의 면적을 위해 가로를 -1 해준 것

    w, h = max_w, max_h

    if temp_idx == idx:
        break

print(answer)

"""
5
13 4
6 5
4 3
11 3
9 5
답 : 42

2
2 4
8 10
답 : 34

5
2 4
4 6
6 8
8 6
10 4
답 : 48
"""
