a = int(input())
b = int(input())
answer = 0
temp = []

prime_list = [i for i in range(2, b + 1)]

for i in range(len(prime_list)):
    if prime_list[i] != 0:
        for j in range(i + 1, len(prime_list)):
            if prime_list[j] % prime_list[i] == 0:
                prime_list[j] = 0
for k in range(a, b + 1):
    if k in prime_list:
        answer += k
        temp.append(k)
if not temp:
    print(-1)
else:
    print(answer)
    print(temp[0])