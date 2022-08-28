str1 = input()
str2 = input()
answer = 0

lst = [[0] * (len(str1) + 1) for _ in range(len(str2) + 1)]

for i in range(1, len(str2) + 1):
    current = str2[i - 1]
    for j in range(1, len(str1) + 1):
        target = str1[j - 1]
        if current == target:
            lst[i][j] = lst[i - 1][j - 1] + 1
        else:
            lst[i][j] = max(lst[i - 1][j], lst[i][j - 1])

print(max(lst[-1]))

