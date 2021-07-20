total_score = 0

for i in range(5):
    score = int(input())
    if score < 40:
        score = 40
    total_score += score

print(total_score // 5)