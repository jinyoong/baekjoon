answer = []
result = []
n, m = map(int, input().split())


def permutation(cnt, choice):

    if cnt == m:
        temp = result[:]
        answer.append(temp)
        return

    for i in range(choice, n+1):
        result.append(i)
        permutation(cnt+1, i)
        result.pop()

    return


permutation(0, 1)

for ans in answer:
    print(*ans)
