"""
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
"""

"""
target = input()


def solution2(start):
    global target
    temp = 0
    idx = start

    while idx < len(target):
        current = target[idx]

        if idx + 1 < len(target) and target[idx + 1] == "(":
            temp_2, end = solution2(idx + 2)
            temp += temp_2 * int(current)
            return temp, end + 1

        if current == ")":
            return temp, idx

        if current != "":
            temp += 1

        idx += 1

    return temp, idx


total_idx = 0
answer = 0

while total_idx < len(target):
    result, temp_idx = solution2(total_idx)
    total_idx = temp_idx
    answer += result

print(answer)
"""

"""
S = input()


def solution3(target):
    answer = 0
    temp = 0
    stack = list(target)

    while stack:
        element = stack.pop()

        if element == ")":
            answer += temp
            temp = 0
            continue

        if element == "(":
            multiple = stack.pop()
            temp *= int(multiple)
            continue

        temp += 1

    answer += temp
    return answer


print(solution3(S))
"""

S = input()


def solution4(target):
    answer = 0
    stack = []

    for ele in target:

        if ele != ")":
            stack.append(ele)
            continue

        temp = 0
        while True:
            inner = stack.pop()

            if inner == "(":
                multiple = int(stack.pop())
                temp *= multiple
                stack.append(temp)
                break

            if inner == int(inner):
                temp += inner
            else:
                temp += 1

    for ele in stack:

        if ele == int(ele):
            answer += ele
        else:
            answer += 1

    return answer


print(solution4(S))


"""
반례
6(12)333
답 : 15

3(3(3(2(2)2(2))))
답 : 108

15(22)13(92(1111)42(222))
답 : 60
"""