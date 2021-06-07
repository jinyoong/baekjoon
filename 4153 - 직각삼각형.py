while True:
    num_list = list(map(int, input().split()))
    if num_list == [0, 0, 0]:
        break
    num_list.sort(reverse=True)
    if num_list[0] ** 2 == num_list[1] ** 2 + num_list[2] ** 2:
        print('right')
    else:
        print('wrong')
