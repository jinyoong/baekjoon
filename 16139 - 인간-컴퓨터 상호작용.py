string = input()
N = int(input())
alphas = {}
targets = []
for _ in range(N):
    a, l, r, = input().split()
    targets.append([a, int(l), int(r)])

    if a not in alphas.keys():
        temp_lst = [0] * len(string)

        if string[0] == a:
            temp_lst[0] = 1

        for i in range(1, len(string)):

            if string[i] == a:
                temp_lst[i] = temp_lst[i - 1] + 1
            else:
                temp_lst[i] = temp_lst[i - 1]

        alphas[a] = temp_lst

for target in targets:
    t, start, end = target

    if start == 0:
        print(alphas[t][end])
    else:
        print(alphas[t][end] - alphas[t][start - 1])
