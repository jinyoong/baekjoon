# 처음 1이 이동하는 부분은 3, 2 가 번갈아서 이동하게 된다
# 즉, 홀수 개인 경우 1은 3부터 가고 짝수 개인 경우 1은 2부터 간다

"""
1. n 개의 원판이 있는 경우에는 n-1 개의 원판을 2번으로 옮긴 뒤, n 번째 원판을 3 번으로 옮겨야 한다.
2. 그럼 이제 n-1 개의 원판을 2 번에서 3 번으로 옮기는 일이 되는 일이 되가지고
3. 1 번에서 얻은 좌표들에서 1을 2로, 2를 1로 바꾸면 될 것 같다
1 개인 경우
1 => 3

2 개인 경우
1 => 2, 여기까지가(1개인 경우)
1 => 3, (n 번째 원판)
2 => 3 이 된다.

3 개인 경우
1 => 3,
1 => 2,
3 => 2, 여기까지가 (2개의 원판을 2 번으로 옮기는 경우)
1 => 3, (n 번째 원판)
2 => 1,
2 => 3,
1 => 3

"""

memo = [[] for _ in range(21)]
memo[1] = [[1, 3]]
memo[2] = [[1, 2], [1, 3], [2, 3]]

for k in range(3, 21):
    temp = [[] for _ in range(2 ** k - 1)]
    t_lst = [lst[:] for lst in memo[k-1]]
    idx = 0

    for ele in t_lst:
        for i in range(2):
            if ele[i] == 3:
                ele[i] = 2
            elif ele[i] == 2:
                ele[i] = 3
        temp[idx] = ele
        idx += 1

    temp[idx] = [1, 3]
    idx += 1

    t2_lst = [lst[:] for lst in memo[k - 1]]

    for ele in t2_lst:
        for i in range(2):
            if ele[i] == 1:
                ele[i] = 2
            elif ele[i] == 2:
                ele[i] = 1
        temp[idx] = ele
        idx += 1

    memo[k] = temp


n = int(input())

print(len(memo[n]))
for ele in memo[n]:
    print(*ele)
