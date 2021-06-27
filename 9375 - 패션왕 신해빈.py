T = int(input())

for i in range(T):
    total_cloth = int(input())

    # 먼저 종류별로 옷을 몇 개씩 가지고 있는지 확인하기 위해
    # 딕셔너리를 종류 : 개수 식으로 항목을 채운다.
    cloth_dict = {}
    for j in range(total_cloth):
        cloth, kinds = map(str, input().split())
        if kinds in cloth_dict:
            cloth_dict[kinds] += 1
        else:
            cloth_dict[kinds] = 1

    # 옷을 입을 수 있는 경우의 수에서 제한되는 조건은
    # 한 종류의 옷은 1벌씩, 최소 1벌 이상 입어야 하는 것이므로
    # n번째 종류의 옷이 k벌 있었다고 한다면 입지 않는다, 1번을 입는다, 2번을 입는다, ''', k번을 입는다의
    # 총 k + 1 가지의 종류가 생긴다.
    # 즉 각 종류별로 가진 옷의 개수에 1을 더한값을 모두 곱한 뒤 알몸이 되는 경우 1을 빼주면 전체 경우의 수가 나온다.

    answer = 1

    for values in cloth_dict.values():
        answer *= values + 1

    answer -= 1

    print(answer)