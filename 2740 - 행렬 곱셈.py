N, M = map(int, input().split())

matrix_a = [[] for _ in range(N)]

for i in range(N):
    matrix_a[i] = list(map(int, input().split()))

M, K = map(int, input().split())

matrix_b = [[] for _ in range(M)]

for i in range(M):
    matrix_b[i] = list(map(int, input().split()))

matrix_result = [[0] * K for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            matrix_result[i][j] += matrix_a[i][k] * matrix_b[k][j]

for i in range(N):
    print(*matrix_result[i])
