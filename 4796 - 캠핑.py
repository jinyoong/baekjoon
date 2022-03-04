test_case = 0

while True:
    test_case += 1
    answer = 0
    P, L, V = map(int, input().split())
    if [P, L, V] == [0, 0, 0]:
        break

    answer += ((V // L) * P)
    if V % L < P:
        answer += V % L
    else:
        answer += P

    print("Case {}: {}".format(test_case, answer))
