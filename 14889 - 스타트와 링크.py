N = int(input())

members = [list(map(int, input().split())) for _ in range(N)]
team_start = []


def point(lst):
    result = 0
    for i in range(N // 2):
        for j in range(N // 2):
            if i == j:
                continue
            result += members[lst[i]][lst[j]]
    return result


def permutation(result, idx, cnt, n):
    if cnt == n:
        team_start.append(result)
        return

    for p in range(idx, N):
        permutation(result + [p], p + 1, cnt + 1, n)


permutation([], 0, 0, N // 2)
answer = 987654321

for k in range(len(team_start) // 2):
    s_p = point(team_start[k])
    l_p = point(team_start[-k-1])
    result = abs(s_p - l_p)
    if answer > result:
        answer = result

print(answer)
