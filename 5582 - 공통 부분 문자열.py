A = input()
B = input()


def solution(string1, string2):
    answer = 0
    result = [0] * (len(string2) + 1)
    new_result = [0] * (len(string2) + 1)

    for i in range(len(string1)):
        for j in range(len(string2)):

            if string1[i] == string2[j]:
                new_result[j + 1] = result[j] + 1

            if new_result[j + 1] > answer:
                answer = new_result[j + 1]

        result = new_result[:]
        new_result = [0] * (len(string2) + 1)

    return answer


print(solution(A, B))
