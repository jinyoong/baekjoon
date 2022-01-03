T = int(input())

numbers = [list(map(int, input().split())) for _ in range(4*T)]

'''
두 대각선의 길이가 같고 두 대각선의 중점이 같고 대각선이 직교하면 정사각형
'''

for i in range(T):
    case1 = [i*4, i*4+1, i*4+2, i*4+3]
    case2 = [i*4, i*4+2, i*4+1, i*4+3]
    case3 = [i*4, i*4+3, i*4+1, i*4+2]
    answer = 0

    for case in [case1, case2, case3]:
        p1, p2, p3, p4 = case
        len_dia_1 = abs(numbers[p1][0] - numbers[p2][0]) ** 2 + abs(numbers[p1][1] - numbers[p2][1]) ** 2
        len_dia_2 = abs(numbers[p3][0] - numbers[p4][0]) ** 2 + abs(numbers[p3][1] - numbers[p4][1]) ** 2
        if len_dia_1 != len_dia_2:
            continue

        mid_1 = [(numbers[p1][0] + numbers[p2][0]), (numbers[p1][1] + numbers[p2][1])]
        mid_2 = [(numbers[p3][0] + numbers[p4][0]), (numbers[p3][1] + numbers[p4][1])]
        if mid_1 != mid_2:
            continue

        if numbers[p1][0] == numbers[p2][0] and numbers[p3][1] == numbers[p4][1]:
            answer = 1
            break

        if numbers[p3][0] == numbers[p4][0] and numbers[p1][1] == numbers[p2][1]:
            answer = 1
            break

        inc_1 = (numbers[p1][1] - numbers[p2][1]) / (numbers[p1][0] - numbers[p2][0])
        inc_2 = (numbers[p3][1] - numbers[p4][1]) / (numbers[p3][0] - numbers[p4][0])
        if abs((inc_1 * inc_2) + 1) > 0.00001:
            continue

        answer = 1
        break

    print(answer)