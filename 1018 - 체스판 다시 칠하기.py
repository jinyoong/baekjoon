N, M = map(int, input().split())

square = []
color_list1 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
              ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
              ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
              ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
              ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
              ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
              ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
              ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
              ]

color_list2 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
              ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
              ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
              ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
              ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
              ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
              ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
              ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

for i in range(N):
    square.append(list(input()))

ct_list = []

for j in range(M):
    if j + 7 >= M:
        break
    else:
        for k in range(N):
            if k + 7 >= N:
                break
            else:
                temp = []
                ct = 0
                ct_1 = 0
                ct_2 = 0
                for c in range(8):
                    temp.append(square[k + c][j: j + 8])
                for t in range(8):
                    for n in range(8):
                        if temp[t][n] != color_list1[t][n]:
                            ct_1 += 1
                        if temp[t][n] != color_list2[t][n]:
                            ct_2 += 1
                if ct_1 <= ct_2:
                    ct = ct_1
                else:
                    ct = ct_2

                # print('{}행 {}열부터 시작하는 8*8 체스판에서 바꿔야 하는 사각형의 숫자는 {}입니다.'.format(k, j, ct))
                ct_list.append(ct)

print(min(ct_list))