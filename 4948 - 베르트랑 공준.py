'''def bertrand(n):
    answer = 0
    for i in range(n + 1, 2 * n + 1):
        for j in range(2, round(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            # print('소수로 {}(이)가 있습니다.'.format(i))
            answer += 1
    return answer'''


m = 2 * 123456 + 1
prime_num = [True] * m
for i in range(2, round(m ** 0.5) + 1):
    if prime_num[i]:
        for j in range(2 * i, m, i):
            prime_num[j] = False

def bert(n):
    answer = 0
    for i in range(n + 1, 2 * n + 1):
        if prime_num[i]:
            answer += 1
    return answer

while True:
    num = int(input())
    if num == 0:
        break
    print(bert(num))