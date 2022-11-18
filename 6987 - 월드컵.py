import sys

custom_input = sys.stdin.readline

lst = [list(map(int, custom_input().split())) for _ in range(4)]


def solution(countries):
    answer = [0, 0, 0, 0]

    for idx, country in enumerate(countries):
        country_result = [0, 0, 0]
        draw_count = 0
        temp = -1

        for i in range(0, 18, 3):
            win, draw, lose = country[i], country[i + 1], country[i + 2]
            temp *= -1

            # print("{}번째의 나라의 승 : {}, 무 : {}, 패 : {}".format(i % 3 + 1, win, draw, lose))

            if win + draw + lose >= 6:
                break

            country_result[0] += win
            country_result[1] += temp * draw
            country_result[2] += lose
            draw_count += draw

        # print(country_result)

        if draw_count % 2:
            continue

        if country_result[0] == country_result[2] and country_result[1] == 0 and draw_count // 2 + country_result[0] == 15:
            answer[idx] = 1

    return answer


print(*solution(lst))
