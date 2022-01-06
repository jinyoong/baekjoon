'''
A 는 B로
B 는 BA로
A가 n 개였고, B가 m 개였을 때
B가 n개, BA가 m 개로 된다
결국에는 A : m 개, B : n + m 개가 된다

'''
K = int(input())

cnt_a = 1
cnt_b = 0
for i in range(K):
    cnt_a, cnt_b = cnt_b, cnt_a + cnt_b

print(cnt_a, cnt_b)
