L = int(input())
target = input()
answer = 0
r = 31
m = 1234567891

for i in range(L):
    temp = ((ord(target[i]) - 96) * r ** i) % m
    answer = (answer + temp) % m

print(answer)
