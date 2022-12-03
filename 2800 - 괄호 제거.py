formula = input()
n = len(formula)


def solution(idx, result, count):

    if idx == n:
        print(result)
        return

    if formula[idx] == "(":
        solution(idx + 1, result, count + 1)
        solution(idx + 1, result + "(", count)

    elif formula[idx] == ")":

        if count == 0:
            solution(idx + 1, result + ")", 0)
        else:
            solution(idx + 1, result, count - 1)

    else:
        solution(idx + 1, result + formula[idx], count)


print(solution(0, "", 0))
