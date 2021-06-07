T = int(input())

for i in range(T):
    num = int(input())
    # 골드바흐의 추측은 두 소수를 이용해야 한다.
    # 두 소수의 합으로 이루어진 쌍을 찾아야 하므로
    # 두 소수 중 작은 수는 무조건 주어진 숫자의 절반보다는 작아야 한다.
    for j in range(int(num / 2), 1, -1):
        for k in range(2, round(j)):
            # 주어진 숫자를 2부터 제곱근까지 봤을 때 약수가 존재한다면 소수가 아니므로
            # 해당 조건식으로 소수인지 판단한다.
            if j % k == 0:
                break
        else:
            for n in range(2, round(num - j)):
                if (num - j) % n == 0:
                    break
            else:
                print(j, num - j)
                break