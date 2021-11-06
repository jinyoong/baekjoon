def solution(numbers):
    points = [[0] * 101 for _ in range(101)]
    # 점을 찍고, 그 점의 개수를 세자
    # 대신 시작점부터 하면 점이 많아지니, 면적을 볼 수 있게 시작점 +1 로 시작하자
    answer = 0

    for ele in numbers:
        for r in range(ele[0]+1, ele[2]+1):
            for c in range(ele[1]+1, ele[3]+1):
                if points[r][c]:
                    continue
                points[r][c] = 1
                answer += 1

    return answer


numbers = [[] for _ in range(4)]

for i in range(4):
    numbers[i] = list(map(int, input().split()))

print(solution(numbers))
