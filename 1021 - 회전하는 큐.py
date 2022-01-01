import sys

input = sys.stdin.readline

N, M = map(int, input().split())
targets = list(map(int, input().split()))
numbers = [i+1 for i in range(N)]

idx = 0
answer = 0

while idx != M:

    if numbers[0] == targets[idx]:
        idx += 1
        numbers.pop(0)
        continue

    for i in range(1, 51):
        if numbers[i] == targets[idx]:
            answer += i
            numbers = numbers[i+1:] + numbers[:i]
            idx += 1
            break

        if numbers[-i] == targets[idx]:
            answer += i
            if i == 1:
                numbers = numbers[:-i]
            else:
                numbers = numbers[-i+1:] + numbers[:-i]
            idx += 1
            break

print(answer)
