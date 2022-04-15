E, S, M = map(int, input().split())
# 1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19
# 1 2 3 이라면 5266
# 19로 나눴을 때 나머지가 3, 28로 나눴을 때 나머지가 2, 15로 나눴을 때 나머지가 1인 경우
if E == 15:
    E = 0
if S == 28:
    S = 0
if M == 19:
    M = 0
number = 0

while True:
    number += 1

    if number % 15 == E and number % 28 == S and number % 19 == M:
        print(number)
        break
