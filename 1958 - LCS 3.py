lst = [list(input()) for _ in range(3)]
lst.sort(key=lambda x: -len(x))


def lcs(long, short):
    result = []
    li = 0
    si = 0
    temp = []

    while si < len(short):

        short_ele = short[si]
        long_ele = long[li]

        if short_ele == long_ele:
            si += 1
            li += 1
            temp.append(short_ele)

            if li >= len(long):
                result.append(temp)
                temp = []
                li = 0
        else:
            li += 1

            if li >= len(long):
                result.append(temp)
                temp = []
                li = 0
                si += 1

    result.append(temp)

    return result


def solution(target_list):
    answer = 0
    new_target_list = lcs(target_list[0], target_list[1])
    print(new_target_list)
    for new_target in new_target_list:

        if len(new_target) > len(target_list[2]):
            result = lcs(new_target, target_list[2])
        else:
            result = lcs(target_list[2], new_target)

        for ele in result:
            if answer < len(ele):
                answer = len(ele)

    return answer


def solution2(target_list):
    result = [[[0] * (len(target_list[0]) + 1) for _ in range(len(target_list[1]) + 1)] for _ in range(len(target_list[2]) + 1)]

    for i in range(1, len(target_list[2]) + 1):
        for j in range(1, len(target_list[1]) + 1):
            for k in range(1, len(target_list[0]) + 1):

                if target_list[0][k - 1] == target_list[1][j - 1] and target_list[0][k - 1] == target_list[2][i - 1]:
                    result[i][j][k] = result[i - 1][j - 1][k - 1] + 1

                else:
                    result[i][j][k] = max(result[i - 1][j][k], result[i][j - 1][k], result[i][j][k - 1])

    return result[-1][-1][-1]


print(solution2(lst))

"""
반례
abc
cb
b

aㄱㄴㄷㄹbcde1111
abㄱㄷㄹㄴcde
ㄱㄴ
"""