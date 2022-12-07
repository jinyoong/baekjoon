import sys

custom_input = sys.stdin.readline


def solution2(idx):
    global is_ok

    if is_ok:
        return

    for k in range(6):
        for t in range(3):
            if result[k][t] > countries[k][t]:
                return

    if idx == 6:
        if result == countries:
            is_ok = True
        return

    country = countries[idx]
    win, draw, lose = country[0], country[1], country[2]

    if win + draw + lose != 5:
        return

    collections2 = set()

    def collection2(cidx, ci, w, d, l, collection_result):
        nonlocal collections2

        if ci == cidx:
            collection2(cidx, ci + 1, w, d, l, collection_result)
            return

        if ci == 6 or w + d + l == 0:
            collections2.add(tuple(collection_result))

        if w:
            collection_result[ci] = 1
            collection2(cidx, ci + 1, w - 1, d, l, collection_result)
            collection_result[ci] = 0

        if d:
            collection_result[ci] = 2
            collection2(cidx, ci + 1, w, d - 1, l, collection_result)
            collection_result[ci] = 0

        if l:
            collection_result[ci] = 3
            collection2(cidx, ci + 1, w, d, l - 1, collection_result)
            collection_result[ci] = 0

    collection2(idx, 0, win, draw, lose, [0, 0, 0, 0, 0, 0])

    for collection_element in collections2:
        for j, ele in enumerate(collection_element):

            if ele == 0:
                continue
            elif ele == 1:
                result[j][2] += 1
            elif ele == 2:
                result[j][1] += 1
            else:
                result[j][0] += 1

        solution2(idx + 1)

        for j, ele in enumerate(collection_element):

            if ele == 0:
                continue
            elif ele == 1:
                result[j][2] -= 1
            elif ele == 2:
                result[j][1] -= 1
            else:
                result[j][0] -= 1


answer = [0, 0, 0, 0]
for ai in range(4):
    countries = []
    lst = list(map(int, custom_input().split()))
    for i in range(0, 18, 3):
        temp = [lst[i], lst[i + 1], lst[i + 2]]
        countries.append(temp)

    result = [[0, 0, 0] for _ in range(6)]
    is_ok = False
    solution2(0)

    if is_ok:
        answer[ai] = 1
    else:
        answer[ai] = 0

print(*answer)


"""
def collection(cidx, w, d, l, collection_result):
    nonlocal collections

    if w == d == l == 0:
        collections.add(tuple(collection_result))

    for ci in range(6):

        if ci == cidx:
            continue

        if collection_result[ci] != 0:
            continue

        if w:
            collection_result[ci] = 1
            collection(cidx, w - 1, d, l, collection_result)
            collection_result[ci] = 0

        if d:
            collection_result[ci] = 2
            collection(cidx, w, d - 1, l, collection_result)
            collection_result[ci] = 0

        if l:
            collection_result[ci] = 3
            collection(cidx, w, d, l - 1, collection_result)
            collection_result[ci] = 0

    return result
"""

"""
3 1 1 1 0 4 1 1 3 3 0 2 3 0 2 3 0 2
3 1 1 1 0 4 1 1 3 3 0 2 3 0 2 3 0 2
3 1 1 1 0 4 1 1 3 3 0 2 3 0 2 3 0 2
3 1 1 1 0 4 1 1 3 3 0 2 3 0 2 3 0 2
"""