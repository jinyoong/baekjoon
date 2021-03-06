T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 두 원의 반지름과 중심 사이의 거리를 이용해 교점이 몇 개인지 판단한다.
    # 교점이 2개인 경우  : 중심사이의 거리 < 반지름의 합 이면서 큰 원 안에 작은 원이 포함되면 안된다.
    if ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5 < r1 + r2 and abs(r1 - r2) < ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5:
        print(2)
    # 교점이 무한대인 경우 : 일치
    elif x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    # 교점이 1개인 경우 : 외접 or 내접
    elif (y2 - y1) ** 2 + (x2 - x1) ** 2 == (r1 + r2) ** 2 or (y2 - y1) ** 2 + (x2 - x1) ** 2 == (r1 - r2) ** 2:
        print(1)
    #교점이 0개인 경우 : 안에 쏙 들어가거나 너무 멀거나
    else:
        print(0)