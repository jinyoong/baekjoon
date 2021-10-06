N, M = map(int, input().split())
a = [0] + list(map(int, input().split())) + [0, 0]
snow_lst = []


def solution(idx, snow, time):

    if time == M or idx >= N:
        return snow_lst.append(snow)

    solution(idx+1, snow+a[idx+1], time+1)
    solution(idx+2, snow//2+a[idx+2], time+1)


solution(0, 1, 0)
print(max(snow_lst))
