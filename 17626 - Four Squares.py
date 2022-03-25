n = int(input())
numbers = [1] * (n+1)

for i in range(2, n+1):
    if i ** (1/2) % 1 == 0:
        continue

    result = n
    for j in range(1, int(i ** (1/2)) + 1):
        # 제곱수의 합으로 만들어야 하니까 제곱수인 경우에만 반복문을 돌려도 된다
        # 만약 4를 더해서 현재 숫자를 만드는 조합을 본다면 i - 4 라는 숫자를 구성하는 제곱수들은
        # 이미 이전에 구해져있을 테니까
        if numbers[i-j**2] < result:
            result = numbers[i-j**2]

    numbers[i] = result + 1

print(numbers[n])
# answer = n
#
#
# def solution(number, result):
#     global answer
#     if number == 0:
#         if answer > result:
#             answer = result
#         return
#
#     start = int(number ** (1/2))
#     for i in range(start, 0, -1):
#         solution(number - i ** 2, result+1)
#
#
# solution(n, 0)
# print(answer)
