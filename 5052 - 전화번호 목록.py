def solution(numbers, n):
    number_dict = dict()

    for number in numbers:

        if not trie(number_dict, number, 0):
            return "NO"

    return "YES"


def trie(target_dict, target_number, k):
    key = target_number[k]
    value = target_number[k + 1] if k + 1 != len(target_number) else "-1"

    if "-1" in target_dict:
        return False

    if value == "-1" and key in target_dict and len(target_dict[key].items()) >= 1:
        return False

    if key not in target_dict:
        target_dict[key] = {value: dict()}
    else:
        if value not in target_dict[key]:
            target_dict[key].update({value: dict()})

    if value == "-1":
        return True

    return trie(target_dict[key], target_number, k + 1)


t = int(input())

for _ in range(t):
    N = int(input())
    lst = [input() for _ in range(N)]
    print(solution(lst, N))
