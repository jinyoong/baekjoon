S = input()


def solution(s, start):
    target = []
    end = len(s)

    for i in range(start, len(s)):

        if i + 1 < len(s) and s[i + 1] == '(':
            count = int(s[i])
            result, end_idx = solution(s, i + 2)
            target += result * count
            return target, end_idx + 1

        if s[i] == ')':
            return target, i

        target += s[i]

    return target, end


answer = []
end_point = 0

while end_point < len(S):
    ans, new_end = solution(S, end_point)
    end_point = new_end
    answer += ans

print(len(answer))
