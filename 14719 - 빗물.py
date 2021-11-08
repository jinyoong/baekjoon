H, W = map(int, input().split())
heights = list(map(int, input().split()))

# 먼저 기준값을 정하고 그 다음 숫자들을 보면서 기준값보다 작은 값이 나오면 초기화 하자
# 그러다가 최솟값보다 크고 기준값보다 작은 값이 나오면 최솟값인 블록들을 해당 값으로 바꿔주고
# 최솟값을 해당 값으로 놓고 기준값 이상이 값이 나올때까지 반복....

standard = 0
min_value = H
answer = 0
check = []
for i in range(W):
    if heights[i] >= standard:  # 현재 높이가 기준값 이상인 경우
        for num in check:  # 높이가 더 낮은 지역이 check 에 저장되어 있으므로
            answer += (standard-num)  # standard 와 각 높이의 차 만큼을 결과에 더해주고
        check = []  # check 를 비워준다
        standard = heights[i]  # 기준값을 현재값으로 바꾸고
        min_value = heights[i]  # 최솟값도 현재값으로 바꿔준다
        continue

    if heights[i] < standard:  # 만약 현재 높이가 기준값 미만인 경우
        if heights[i] <= min_value:  # 동시에 현재 높이가 최솟값 이하인 경우
            min_value = heights[i]  # 최솟값을 현재 높이로 바꿔준다

        elif heights[i] > min_value:  # 현재 높이가 최솟값보다는 큰 경우
            for j in range(len(check)):  # check 에 저장된 값들 중 적어도 한 값보다는 크다는 의미이므로
                diff = max(heights[i]-check[j], 0)  # check 에 저장된 각 값들의 차를 구한다
                answer += diff
                check[j] += diff
        check.append(heights[i])

print(answer)


'''
예시 코드들
4 8
0 1 0 1 4 1 2 1
출력: 2

4 4
3 0 1 4
출력: 5

4 8
3 1 2 3 4 1 1 2
출력: 5

3 5
0 0 0 2 0
출력: 0

10000 76
992 3508 6427 8970 1683 2114 3762 5945 8251 8349 2672 1813 2294 4623 1089 1724 5577 2362 5035 5028 3344 9321 3104 8877 2534 5864 9791 3221 5571 8763 773 6687 4909 3330 1427 8554 9688 6293 1899 3573 8597 5976 2772 1410 5182 888 4671 8106 782 6735 2832 9642 9824 1203 858 2643 2024 3798 5114 4253 72 2427 7137 1488 7324 4837 3656 6194 2600 8530 2413 5892 6404 7682 6775 7467
출력: 316105

100 18
28 100 43 33 37 100 87 15 52 35 54 86 60 24 99 56 4 40
출력: 602
'''