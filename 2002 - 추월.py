N = int(input())
dct = dict()
for i in range(N):
    car = input()
    dct[car] = i

lst = [input() for _ in range(N)]


def solution(n, in_car, out_car):
    answer = 0
    count = 0

    for j in range(n - 1, -1, -1):
        out_car_element = out_car[j]

        if j == n - 1:
            count = in_car[out_car_element]
            continue

        if in_car[out_car_element] < count:
            count = in_car[out_car_element]
            continue

        else:
            answer += 1

    return answer


print(solution(N, dct, lst))
