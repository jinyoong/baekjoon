def solution(idx, result):
    '''
    idx : 다음 번 밟은 계단의 번호, -1부터 시작
    result : 밟은 계단의 점수 합
    만약 visited 에 번호가 연속한 3개가 나오게 되면 해당 계단은 밟지 않는다
    '''
    global answer

    if idx >= 2:
        if visited[idx] == 1 and visited[idx-1] == 1 and visited[idx-2] == 1:
            return

    if idx == N-1:  # 마지막 계단을 밟은 경우
        if result > answer:
            answer = result
        return

    visited[idx+1] = 1
    solution(idx+1, result+stairs[idx+1])
    visited[idx+1] = 0

    if idx + 2 >= N:
        return

    visited[idx+2] = 1
    solution(idx+2, result+stairs[idx+2])
    visited[idx+2] = 0


N = int(input())
stairs = [int(input()) for _ in range(N)]
answer = 0
visited = [0] * N
solution(-1, 0)
print(answer)
