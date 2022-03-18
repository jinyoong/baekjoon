def solution():
    numbers = [0] * 12
    numbers[1] = numbers[2] = numbers[3] = 1
    for i in range(2, 12):
        if i-3 >= 1:
            numbers[i] += numbers[i-3]

        if i-2 >= 1:
            numbers[i] += numbers[i-2]

        numbers[i] += numbers[i-1]

    return numbers


T = int(input())

answers = solution()

for _ in range(T):
    n = int(input())
    print(answers[n])
