def solution(n1, n2):

    visited = {n1}  # 촌수를 계산한 사람들을 담을 셋
    queue = [(n1, 0)]  # 살펴볼 사람들을 담을 큐
    rear = 1
    head = 0

    while head < rear:  # 큐가 빌 때까지 반복
        p, answer = queue[head]  # 현재 사람과 촌수 저장
        head += 1

        if p == n2:  # 만약 찾는 사람이 나오면 촌수 반환
            return answer

        for num in relations[p]:  # 해당 사람의 부모와 자식들을 하나씩 살펴본다
            if num != -1:  # -1은 주어진 사람들 중 부모가 없다는 뜻....
                if num not in visited:  # 한 번도 촌수를 계산하지 않은 사람이라면
                    queue.append((num, answer+1))  # 현재 촌수에 1을 더하여 큐에 저장
                    rear += 1
                    visited.add(num)

    return -1


n = int(input())
a, b = map(int, input().split())
m = int(input())
relations = [[-1] for _ in range(n+1)]  # 부모는 맨 앞 자시들은 1번 인덱스부터
for _ in range(m):
    x, y = map(int, input().split())
    relations[y][0] = x
    relations[x].append(y)
print(solution(a, b))
