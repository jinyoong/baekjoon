N = int(input())

for i in range(N):
    ox_list = list(input())
    ox_score_list = []
    ox_score = 0
    answer = 0
    for j in range(len(ox_list)):
        if ox_list[j] == 'O':
            ox_score += 1
            ox_score_list.append(ox_score)
        else:
            ox_score_list.append(0)
            ox_score = 0
        answer += ox_score
    print(answer)
