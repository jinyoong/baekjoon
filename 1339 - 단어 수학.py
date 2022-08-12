N = int(input())
words = [input() for _ in range(N)]
numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


def solution():
    answer = 0
    result = [{} for _ in range(8)]
    alpha = {}

    for word in words:
        for i in range(len(word)):
            result[8 - len(word) + i][word[i]] = result[8 - len(word) + i].get(word[i], 0) + 1
            alpha[word[i]] = 0

    for j in range(8):

        if not result[j]:
            continue

        for key, value in result[j].items():
            alpha[key] += 10 ** (7 - j) * value

    alpha_sort = sorted(alpha.items(), key=lambda x: x[1], reverse=True)
    idx = 0
    for alpha_sort_ele in alpha_sort:
        answer += alpha_sort_ele[1] * numbers[idx]
        idx += 1

    return answer


print(solution())


"""
10
ABB
BB
BB
BB
BB
BB
BB
BB
BB
BB

답 : 1790
"""
