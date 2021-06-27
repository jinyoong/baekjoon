T = int(input())

for i in range(T):
    a, b = map(int, input().split())

    # 다리끼리는 겹쳐질 수 없다.
    # 즉, 동쪽이랑 연결할 다리 밑에 남아있는 사이트의 개수가 서쪽에 남아있는 사이트보다 많아야 한다.
    # 따라서 동쪽의 사이트 M개 중에서 서쪽의 사이트와 연결할 N개를 순서에 상관없이 뽑는 것과 같다.
    # 예를 들어 8개 중에 4개를 순서에 상관없이 뽑은 뒤 위에 있는 순서대로 놓으면 되는 거니까

    n = 1
    k = 1
    for i in range(b, b-a, -1):
        n *= i

    for i in range(1, a+1):
        k *= i

    print(n//k)