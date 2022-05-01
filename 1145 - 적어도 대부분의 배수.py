numbers = list(map(int, input().split()))

answer = 1

while True:
    cnt = 0
    for i in range(5):
        if answer % numbers[i] == 0:
            cnt += 1
        
    if cnt >= 3:
        print(answer)
        break
    
    answer += 1
