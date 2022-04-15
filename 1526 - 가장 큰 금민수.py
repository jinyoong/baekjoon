N = int(input())

while True:
    for ele in str(N):
        if ele not in {'4', '7'}:
            break
    else:
        print(N)
        break

    N -= 1
