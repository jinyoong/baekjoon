N, K = map(int, input().split())


def solution(start, end):
    queue = [(start, 0)]
    idx = 0
    length = 1
    visited = {start: 0}

    while idx < length:
        current, time = queue[idx]
        idx += 1

        if current == end:
            return time

        for i, new_point in enumerate([current * 2, current + 1, current - 1]):
            new_time = time + 1 if i else time

            if new_point < 0:
                continue

            if end < current and i < 2:
                continue

            if visited.get(new_point, 987654321987654321) <= new_time:
                continue

            if i == 0:  # 순간이동 하는 경우는 시간 증가량이 없으므로 최우선적으로 탐색해야 한다
                queue.insert(idx + 1, (new_point, new_time))
            else:
                queue.append((new_point, new_time))
            visited[new_point] = new_time
            length += 1


print(solution(N, K))
