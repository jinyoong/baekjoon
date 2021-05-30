alpha_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS',
              'TUV', 'WXYZ']

s = list(input())
answer = 0

for i in range(len(s)):
    for j in range(len(alpha_list)):
        if s[i] in alpha_list[j]:
            answer += (j + 3)
            break
print(answer)
