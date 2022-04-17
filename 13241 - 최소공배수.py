A, B = map(int, input().split())
answer = 1

while True:
    for i in range(2, min(A, B) + 1):
        if A % i == 0 and B % i == 0:
            A //= i
            B //= i
            answer *= i
            break
    else:
        answer *= A * B
        break

print(answer)
