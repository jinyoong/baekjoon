a, b = map(int, input().split())

prime_list = [1] * (b + 1)

for i in range(2, int(b ** 0.5) + 1):
    if prime_list[i] == 1:
        for j in range(2 * i, b + 1, i):
            prime_list[j] = 0

for i in range(a, b + 1):
    if prime_list[i] == 1 and i != 1:
        print(i)