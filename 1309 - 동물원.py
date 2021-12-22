# def arrange(temp, row, cnt, maximum):
#     global answer
#     if cnt == maximum:
#         answer += 1
#         return
#
#     for r in range(row, N):
#         for c in range(2):
#             if r == 0:
#                 temp[r][c] = 1
#                 arrange(temp, r + 1, cnt + 1, maximum)
#                 temp[r][c] = 0
#                 continue
#             if temp[r-1][c] == 1 or temp[r][(c+1) % 2] == 1:
#                 continue
#             temp[r][c] = 1
#             arrange(temp, r+1, cnt+1, maximum)
#             temp[r][c] = 0
#
#
# N = 6
# answer = 0
# cage = [[0, 0] for _ in range(N)]
# for i in range(N+1):
#     temp = [cage[j][:] for j in range(N)]
#     arrange(temp, 0, 0, i)
#
# print(answer)

N = int(input())
cage = [0] * 100001
cage[1] = 3
cage[2] = 7
cage[3] = 17
cage[4] = 41

if N <= 4:
    print(cage[N])
else:
    for i in range(5, N+1):
        cage[i] = (cage[i-1] * 2 + cage[i-2]) % 9901
    print(cage[N])

'''
N = 1 인 경우 : 3
0 마리 : 1가지
1 마리 : 2가지

N = 2 인 경우 : 7
0 마리 : 1가지
1 마리 : 4가지 (2 * N)
2 마리 : 2가지

N = 3 인 경우 : 17
0 마리 : 1가지
1 마리 : 6가지 (2 * N)
2 마리 : 8가지 (4 * (N - 1))
3 마리 : 2가지

N = 4 인 경우 : 41
0 마리 : 1가지
1 마리 : 8가지 (2 * N)
2 마리 : 18가지 (2마리가 세로로 딱 붙어있게 2줄 고르는 경우: 3가지 => 6가지,  1칸 이상 떨어지게 고르는 경우 4C2 - 3 : 3가지 => 12가지)
3 마리 : 12가지 (4 * (N - 1))
4 마리 : 2가지

N = 5 인 경우 : 99
0 마리 : 1가지
1 마리 : 10가지 (2 * N)
2 마리 : 32가지 (2마리가 세로로 딱 붙어있게 2줄 고르는 경우: 4가지 => 8가지, 1칸 이상 떨어지게 고르는 경우 5C2 - 4 : 6가지 => 24가지)
3 마리 : 38가지 (3마리가 세로로 딱 붙어있게 3줄 고르는 경우: 3가지 => 6가지, 4줄에 3마리 넣는 경우: 12가지 => 24가지, 5줄 양 끝에 1마리씩 넣고 사이 3줄에 1마리 넣는 경우: 2 * 6 - 4 => 8가지)
4 마리 : 16가지 (4 * (N - 1))
5 마리 : 2가지

N = 6 인 경우 : 239
0 마리 : 1가지
1 마리 : 12가지 (2 * N)
2 마리 : 50가지 (2마리가 세로로 딱 붙어있게 2줄 고르는 경우: 5가지 => 10가지, 1칸 이상 떨어지게 고르는 경우 6C2 - 5 : 10가지 => 40가지)
3 마리 : 
4 마리 : 
5 마리 : 20가지
6 마리 : 2가지
이유는 모르겠는데 f(n) = f(n-1) * 2 + f(n-2) 인 것 같다
'''