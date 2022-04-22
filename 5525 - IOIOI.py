N = int(input())

S = int(input())

string = input()

len_pn = N * 2 + 1

result = 0
check = [0] * S

for i in range(1, S):
    if string[i] == 'I':
        check[i] = 1

    if string[i] != string[i-1]:
        check[i] = check[i-1] + 1

    if check[i] >= len_pn and check[i] % 2:
        result += 1

print(result)
