T = int(input())

for i in range(T):
    # print('{}번째 숫자를 입력하시오'.format(i + 1))
    start, finish = map(int, input().split())
    # 먼저 두 지점 간의 거리를 구한다.
    length = finish - start
    if length == 1:
        print(1)
    else:
        length -= 2
        # 맨 처음과 맨 끝은 무조건 1씩 이동하므로 총 거리에서 2를 빼준다.
        # 이제 앞과 뒤를 한 번씩 번갈아 본다.
        # 가장 적게 이동하여 도착하기 위해선 주어진 기회에 최대한 많은 거리를 가는게 좋다
        # 따라서 앞과 뒤를 기준으로 n번째 이동 시 n만큼 이동하는게 최대한 적은 이동으로 도착하게 된다.
        # 2번째 이동부터 시작하므로 이동해야 하는 거리의 초기값을 2로 저장한다.
        move = 2
        # 앞으로 가능한 최대 이동거리, 즉 전의 이동거리 + 1 이다.
        answer = 2
        while length > 0:
            # print('총 거리 : {}, 가능한 최대 이동 거리 : {}, 총 작동 횟수 : {}'.format(length, move, answer))
            if length >= move * 2:
                length -= (2 * move)
                move += 1
                answer += 2
            elif length == (move - 1) + move:
                length -= 2 * move - 1
                answer += 2
            elif length == 2 * (move - 1) and length != move:
                length -= 2 * (move - 1)
                answer += 2
            else:
                length -= move
                answer += 1
        print(answer)

