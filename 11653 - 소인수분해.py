def factorization(n):
    temp = n
    prime_num = [True] * (n + 1)
    for i in range(2, n + 1):
        if prime_num[i]:
            while temp % i == 0:
                print(i)
                temp /= i
            if temp == 1:
                break
            for j in range(2 * i, n + 1, i):
                prime_num[j] = False


num = int(input())
factorization(num)