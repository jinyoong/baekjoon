x_dict = {}
y_dict = {}

for i in range(3):
    a, b = map(int, input().split())
    if a not in x_dict:
        x_dict[a] = 1
    else:
        x_dict[a] += 1
    if b not in y_dict:
        y_dict[b] = 1
    else:
        y_dict[b] += 1

answer = []

for i in x_dict.keys():
    if x_dict[i] == 1:
        answer.append(i)
        break
for i in y_dict.keys():
    if y_dict[i] == 1:
        answer.append(i)
        break
print(*answer)