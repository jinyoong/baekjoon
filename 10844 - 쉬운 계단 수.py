N = int(input())


def solution():

    if N == 1:
        return 9

    answer = 0

    queue = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    idx = 0
    minimum = 10 ** (N - 1)
    maximum = 10 ** N - 1

    while True:

        num = queue[idx]
        idx += 1

        if num > maximum:
            return answer % 1000000000

        add_num_lst = [num % 10 - 1, num % 10 + 1]

        for add_num in add_num_lst:
            if 0 <= add_num < 10:
                new_num = num * 10 + add_num
                queue.append(new_num)

                if minimum <= new_num < maximum:
                    answer += 1


# print(solution())


def solution2():
    # 0으로 끝나는 숫자의 경우 뒤에 1만 붙일 수 있고, 9로 끝나는 숫자의 경우 뒤에 8만 붙일 수 있다
    # 그 외의 숫자들은 두 개씩 붙일 수 있다

    number = [1] * 10  # 끝 자리가 idx 로 끝난 계산수의 개수를 저장할 리스트
    number[0] = 0

    new_number = [0] * 10

    for _ in range(N - 1):
        for i in range(10):
            if i == 0:
                new_number[i + 1] += number[i]

            elif 1 <= i <= 8:
                new_number[i - 1] += number[i]
                new_number[i + 1] += number[i]

            else:
                new_number[i - 1] += number[i]

        number = new_number
        new_number = [0] * 10

    return sum(number) % 1000000000


print(solution2())
