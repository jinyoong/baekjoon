T = int(input())

for _ in range(T):
    N = int(input())
    # number1 = list(map(int, input().split()))
    # note1 = {}
    #
    # for number in number1:
    #     note1[number] = note1.get(number, 0) + 1
    number1 = set(map(int, input().split()))

    M = int(input())
    number2 = list(map(int, input().split()))

    for number in number2:
        print(1 if number in number1 else 0)
