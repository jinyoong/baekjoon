n = int(input())

i = 1
answer = 1

if n == 1:
    answer = 1
else:
    start_num = 2
    ct = 6
    while not (start_num <= n and n <= start_num + ct - 1):
        # 벌집이 시작하는 숫자는 2, 8, 20, 38 순으로 차이가 6, 12, 18, 24 순으로 증가한다.
        # 또한 중앙으로 부터 1칸 멀어질 때마다 둘러싼 칸의 개수도 6개씩 증가해서 6, 12, 18, 24 순으로 증가한다.
        # 따라서 2 ~ 7, 8 ~ 19, 20 ~ 37, 38 ~ 61 순으로 둘러싸게 된다
        # print('{} ~ {}안에 있는지 살핍니다.'.format(start_num, start_num + ct - 1))
        start_num += (6 * i)
        ct += 6
        i += 1
    answer += i
print(answer)