N = int(input())

stick_list = [64]

while True:
    if sum(stick_list) == N:
        print(len(stick_list))
        break
    # print(f'현재 가장 짧은 막대의 길이는 {stick_list[0]}')
    stick = stick_list[0] // 2
    # print(f'가장 짧은 막대를 절반으로 자른 길이는 {stick}')
    stick_list[0] = stick
    # print(stick_list)
    if sum(stick_list) >= N:
        # print(f'절반 중 하나와 남아있는 다른 막대들을 모두 합친 길이는 {N}보다 큽니다')
        pass
    else:
        # print(f'절반 중 하나와 남아있는 다른 막대들을 모두 합친 길이가 {N}보다 작습니다')
        stick_list.insert(0, stick)
