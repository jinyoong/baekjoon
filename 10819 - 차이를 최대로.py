# 짝수(n)개의 숫자가 있는 경우
# -a0 + 2a1 - 2a2 + 2a3 - ... -2an-2 + an-1
# 숫자들을 큰 순서대로 a1, a3, ... an-1 까지 넣은 뒤, a0, a2, a4 순으로 위치하면 된다

# 홀수(n)개의 숫자가 있는 경우
# -a0 + 2a1 - 2a2 + ... + 2an-2 - an-1
# 숫자들을 큰 순서대로 a1, a3, ..., an-2 까지 넣은 뒤, a0, an-1, a2, a4 순으로 넣으면 된다.

n = int(input())

numbers = list(map(int, input().split()))

used = [0] * n

temp = [0] * n

answer = 0

# def solution(temp):
#
#     numbers = sorted(temp, key=lambda x: x, reverse=True)
#
#     answer = 0
#     mid = n // 2
#
#     if n % 2:
#         for i in range(n):
#             if i < mid:
#                 answer += 2 * numbers[i]
#             elif mid <= i < mid + 2:
#                 answer -= numbers[i]
#             else:
#                 answer -= 2 * numbers[i]
#
#     else:
#         for i in range(n):
#             if i < mid - 1:
#                 answer += 2 * numbers[i]
#             elif i == mid - 1:
#                 answer += numbers[i]
#             elif i == mid:
#                 answer -= numbers[i]
#             else:
#                 answer -= 2 * numbers[i]
#
#     return answer
#
#
# print(solution(numbers))


def solution2(numbers, idx, temp):
    global answer

    if idx == len(numbers):
        result = 0
        for i in range(1, n):
            result += abs(temp[i] - temp[i-1])
        if answer < result:
            answer = result
        return

    for i in range(n):
        if not used[i]:
            temp[idx] = numbers[i]
            used[i] = 1
            solution2(numbers, idx+1, temp)
            used[i] = 0


solution2(numbers, 0, temp)
print(answer)


'''
6
20 1 15 8 4 10 => 8 20 1 15 4 10
: correct = 62

6
-5 0 -4 -3 -3 -2 
: correct = 14, wrong = 13

5
2 0 0 -1 3 
: correct = 12, wrong = 11

6
2 -4 -4 0 1 4 
: correct = 29, wrong = 28

4
0 -1 -4 5 
: correct = 19, wrong = 17

6
-5 -3 2 1 -5 5 
: correct = 38, wrong = 37

4
1 -3 -4 4 
: correct = 20, wrong = 19

4
2 3 4 -1 
: correct = 11, wrong = 10

4
-1 -5 2 1 
: correct = 16, wrong = 15

4
-2 1 -1 0 
: correct = 7, wrong = 6

5
-1 -1 0 -3 -4 => -1 -4 0 -3 -1
: correct = 12, wrong = 11'''
