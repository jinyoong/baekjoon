A, B, C = map(int, input().split())


def solution(number, count, divide):
    # A^5%C = (A^2%C * A^3%C)%C
    # A^3%C = ((A%C * A%C)%C * A%C)%C
    # A^2%C = (A%C * A%C)%C

    if count == 1:
        return number % divide

    new_number = solution(number, count // 2, divide)
    if count % 2:
        return ((new_number % divide * new_number % divide) % divide * number % divide) % divide
    else:
        return (new_number % divide * new_number % divide) % divide

    # new_number_1 = solution(number, half_1, divide)
    # new_number_2 = solution(number, half_2, divide)
    # return ((new_number_1 % divide) * (new_number_2 % divide)) % divide
    # 주석 처리 된 부분이랑 12 - 16 코드에서 왜 시간 차이가 나는지 궁금


print(solution(A, B, C))
