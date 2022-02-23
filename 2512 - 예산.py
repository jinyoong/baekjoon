checked = set()


def find_max_budget(numbers, target, min_value, max_value):
    middle = (min_value + max_value) // 2
    sum_value = 0
    for number in numbers:
        sum_value += number if number <= middle else middle

    if sum_value in checked or sum_value == target:
        return middle

    checked.add(sum_value)

    if sum_value > target:
        return find_max_budget(numbers, target, min_value, middle)
    else:
        return find_max_budget(numbers, target, middle, max_value)


N = int(input())

budgets = list(map(int, input().split()))
total = int(input())

sum_amount = 0
max_budget = 0
min_budget = 100000

for budget in budgets:
    if max_budget < budget:
        max_budget = budget

    if min_budget > budget:
        min_budget = budget

    sum_amount += budget

if sum_amount > total:
    print(find_max_budget(budgets, total, 0, max_budget+1))

else:
    print(max_budget)

# 실패한 테스트 케이스
# 6
# 77 89 61 118 91 142
# 120
