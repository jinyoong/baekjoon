T = int(input())

answer = 0

for t in range(T):

    s = list(input())
    s_ele = [s[0]]

    global i
    if len(s) == 1:
        answer += 1
    else:
        for i in range(1, len(s)):

            if s[i - 1] != s[i]:
                if s[i] not in s_ele:
                    s_ele.append(s[i])
                else:
                    i = -1
                    break
        if i == len(s) - 1:
            answer += 1
print(answer)