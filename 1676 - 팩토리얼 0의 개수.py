n = int(input())

# 0의 개수는 해당 숫자를 소인수 분해 했을 때 나오는 (2 * 5)쌍의 지수만큼 나온다.
# 예를 들어 6! = 720 = (2 * 5) * 3^2 * 2^3 이므로 0이 1개 존재하는 것이다.
# 따라서 n!을 이루는 숫자를 하나씩 보며 5와 2의 거듭제곱의 개수를 구하면 된다.

f_ct = 0
t_ct = 0

# 각 숫자가 5 또는 2의 배수일 경우에 5와 2를 몇 개씩 가지는지 세서 저장하자
for i in range(n, 1, -1):
    if i % 5 == 0 or i % 2 == 0:
        test_f = i
        test_t = i
        while test_f % 5 == 0:
            f_ct += 1
            test_f /= 5
        while test_t % 2 == 0:
            t_ct += 1
            test_t /= 2

if f_ct <= t_ct:
    total_ct = f_ct
else:
    total_ct = t_ct

print(total_ct)
