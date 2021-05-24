N = int(input())

score_list = list(map(int, input().split()))
score_sum = 0

for i in score_list:
    score_sum += i


print((score_sum/max(score_list) * 100)/N)