p = [0] * 101

p[1] = p[2] = p[3] = 1
p[4] = 2
for i in range(5, 101):
    p[i] = p[i-1] + p[i-5]

N = int(input())

for _ in range(N):
    t = int(input())
    print(p[t])
