T = int(input())

for i in range(T):
    score_sum = 0
    score_list = list(map(int, input().split()))
    for k in range(1, score_list[0] + 1):
        score_sum += score_list[k]
    mean = score_sum / score_list[0]

    mean_over_ct = 0
    for j in range(1, score_list[0] + 1):
        if score_list[j] > mean:
            mean_over_ct += 1
    print('%0.3f%%' % (mean_over_ct / score_list[0] * 100))