like_fibo = [1] * 118

for i in range(4, 117):
    like_fibo[i] = like_fibo[i-1] + like_fibo[i-3]

n = int(input())
print(like_fibo[n])
