def solution():
    answer = [0] * N
    answer[0] = 1
    ans_idx = 1
    popped = [0] * N
    idx = 0

    while True:
        popped[idx] = 1
        move = balloons[idx]

        if popped == [1] * N:
            break

        for i in range(abs(move)):  # 이동해야 하는 만큼 반복

            if move > 0:  # 오른쪽으로 갈지, 왼쪽으로 갈지 결정
                m = 1  # 오른쪽
            else:
                m = -1  # 왼쪽

            idx = (idx + m) % N  # 해당 방향으로 1칸 가본다
            while popped[idx] == 1:  # 터진 풍선을 지나갈 때는 이동으로 안 치게 된다
                idx = (idx+m) % N  # 터지지 않는 풍선을 만날 때만 1씩 이동

        answer[ans_idx] = idx + 1
        ans_idx += 1

    return answer


N = int(input())

balloons = list(map(int, input().split()))
print(*solution())
