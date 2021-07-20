T = int(input())

name_list = []
pattern = []

for i in range(T):
    name = input()
    name_list.append(name)
    if i == 0:
        pattern = list(name)

answer = ''

for i in range(len(pattern)):
    next_alpha = ''
    for j in range(1, T):
        if pattern[i] != name_list[j][i]:
            next_alpha = '*'
            break
    if next_alpha:
        answer += '?'
    else:
        answer += pattern[i]

print(answer)