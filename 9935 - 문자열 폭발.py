A = input()
B = input()


def solution(target, explosion):
    answer = ""
    result = [-1] * len(target)
    idx = 0
    is_explosion = True

    while is_explosion:
        is_explosion = False

        for i, ele in enumerate(target):

            if result[i] == -2:
                continue

            if ele == explosion[idx]:
                result[i] = idx
                idx += 1
            else:
                idx = 0

                if ele == explosion[idx]:
                    result[i] = idx
                    idx += 1

            if idx == len(explosion):
                is_explosion = True
                count = len(explosion) - 1
                for j in range(i, -1, -1):

                    if count == - 1 and result[j] != -2:
                        idx = result[j] + 1
                        break

                    if result[j] == count:
                        count -= 1
                        result[j] = -2

                else:
                    idx = 0

        idx = 0

    for i, ele in enumerate(target):

        if result[i] == -2:
            continue

        answer += ele

    if not answer:
        answer = "FRULA"

    return answer


def solution2(target, explosion):
    new_target = ""
    result = [-1] * len(target)
    is_explosion = True

    while is_explosion:
        idx = 0
        is_explosion = False

        for i, ele in enumerate(target):

            if ele == explosion[idx]:
                result[i] = idx
                idx += 1
            else:
                idx = 0

                if ele == explosion[idx]:
                    result[i] = idx
                    idx += 1

            if idx == len(explosion):
                is_explosion = True
                count = len(explosion) - 1
                for j in range(i, -1, -1):

                    if count == - 1 and result[j] != -2:
                        idx = result[j] + 1
                        break

                    if result[j] == count:
                        count -= 1
                        result[j] = -2

                else:
                    idx = 0

        for i, ele in enumerate(target):
            if result[i] != -2:
                new_target += ele

            result[i] = -1

        target = new_target
        new_target = ""

    if not target:
        return "FRULA"
    else:
        return target


def solution3(target, explosion):
    target_lst = list(target)
    target_length = len(target)
    result = [-1] * len(target)
    is_explosion = True
    explosion_length = len(explosion)

    while is_explosion:
        idx = 0
        is_explosion = False

        for i, ele in enumerate(target_lst):

            if i >= target_length:
                break

            if ele == explosion[idx]:
                result[i] = idx
                idx += 1
            else:
                idx = 0

                if ele == explosion[idx]:
                    result[i] = idx
                    idx += 1

            if idx == explosion_length:
                is_explosion = True
                count = explosion_length - 1
                for j in range(i, -1, -1):

                    if count == - 1 and result[j] != -2:
                        idx = result[j] + 1
                        break

                    if result[j] == count:
                        count -= 1
                        result[j] = -2

                else:
                    idx = 0

        t_idx = 0
        for i, ele in enumerate(target_lst):
            if i >= target_length:
                break

            if result[i] != -2:

                target_lst[t_idx] = target_lst[i]
                t_idx += 1

            result[i] = -1

        target_length = t_idx

    answer = []
    for i in range(target_length):
        answer.append(target_lst[i])

    if not answer:
        return "FRULA"
    else:
        return "".join(answer)


def solution4(target, explosion):
    answer = [(-1, "")]

    for ele in target:

        idx = answer[-1][0]

        if ele == explosion[idx + 1]:
            answer.append((idx + 1, ele))
        else:
            idx = -1

            if ele == explosion[idx + 1]:
                answer.append((idx + 1, ele))
            else:
                answer.append((idx, ele))

        if answer[-1][0] == len(explosion) - 1:
            for _ in range(len(explosion)):
                answer.pop()

    if len(answer) == 1:
        return "FRULA"
    else:
        result = ""
        for i, ele in answer:
            if ele:
                result += ele
        return result


print(solution4(A, B))
