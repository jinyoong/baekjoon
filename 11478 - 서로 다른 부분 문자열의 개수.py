target = input()
answer = set()

for i in range(len(target)):
    for j in range(i + 1, len(target) + 1):
        answer.add(target[i:j])

print(len(answer))
