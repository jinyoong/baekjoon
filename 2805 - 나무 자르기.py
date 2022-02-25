check = set()


def max_height(numbers, target, min_value, max_value):
    middle = (min_value + max_value) // 2
    sum_value = 0

    for number in numbers:
        sum_value += (number - middle) if number > middle else 0

    if sum_value in check or sum_value == target:
        return middle

    check.add(sum_value)

    if sum_value < target:
        return max_height(numbers, target, min_value, middle)
    else:
        return max_height(numbers, target, middle, max_value)


N, M = map(int, input().split())

trees = list(map(int, input().split()))

maximum = 0

for tree in trees:
    if maximum < tree:
        maximum = tree

print(max_height(trees, M, 0, maximum+1))



