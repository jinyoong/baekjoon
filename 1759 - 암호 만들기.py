L, C = map(int, input().split())

alphas = list(input().split())
alphas.sort()

answer = []
moum = {"a", "e", "i", "o", "u"}


def permutation(result, cnt, idx, moum_cnt):
    if cnt == L:
        if moum_cnt >= 1 and L - moum_cnt >= 2:
            answer.append(result)
        return

    for i in range(idx, C):
        permutation(result + alphas[i], cnt + 1, i + 1, moum_cnt + 1 if alphas[i] in moum else moum_cnt)


permutation("", 0, 0, 0)
for ans in answer:
    print(ans)
