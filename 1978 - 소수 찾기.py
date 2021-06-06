T = int(input())

num_list = list(map(int, input().split()))
answer = 0

prime_list = [i for i in range(2, 1001)]

for i in range(len(prime_list)):
    if prime_list[i] != 0:
        for j in range(i + 1, len(prime_list)):
            if prime_list[j] % prime_list[i] == 0:
                prime_list[j] = 0

for i in range(T):
    if num_list[i] in prime_list:
        answer += 1

print(answer)