T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    floor = [i + 1 for i in range(n)]
    # 0 층에 사는 사람들의 수부터 먼저 리스트로 만들어 준다.
    if k == 0:
        # 만약 해당 사람이 0층 n호에 살고 있다면 그냥 n명이 살면 된다.
        print(floor[n - 1])
    else:
        # 0층이 아니라면 아래층의 사람들의 합을 구해야 한다.
        for j in range(k):
            temp = 0
            for m in range(n):
                temp += floor[m]
                floor[m] = temp
        print(floor[n - 1])