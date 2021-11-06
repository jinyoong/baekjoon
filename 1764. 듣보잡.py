N, M = map(int, input().split())

not_listen = set()

for i in range(N):
    not_listen.add(input())

answer = 0
lst = []
for i in range(M):
    temp = input()
    if temp in not_listen:
        lst.append(temp)
        answer += 1

print(answer)
lst.sort()
for ele in lst:
    print(ele)
