C, N = map(int, input().split())
p_lst = [0] * 1000001

lst = [[] for _ in range(N)]
for i in range(N):
    lst[i] = list(map(int, input().split()))


def solution():
    for idx in range(1, 1000001):
        for ele in lst:
            cost, cnt = ele

            if idx < cost:
                continue

            if p_lst[idx - cost] + cnt >= C:
                return idx

            if not p_lst[idx]:
                p_lst[idx] = p_lst[idx-cost] + cnt
                continue

            if p_lst[idx]:
                p_lst[idx] = max(p_lst[idx-cost] + cnt, p_lst[idx])


print(solution())
