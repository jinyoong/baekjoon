while True:
    number = input()
    if number == '0':
        break

    cnt = len(number) // 2
    for i in range(cnt):
        if number[i] != number[len(number) - i - 1]:
            print('no')
            break
    else:
        print('yes')
