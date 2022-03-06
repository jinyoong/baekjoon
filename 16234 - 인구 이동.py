import sys


def moving():
    answer = 0

    while True:
        answer += 1
        check = set()
        is_change = False
        queue = [[] for _ in range(3000)]
        # queue 를 매 반복마다 새롭게 만드니까 메모리 낭비, 시간 낭비가 발생하는 듯
        # 맨 처음에 길게 만들어놓고 이용해보기
        head = 0
        rear = 0
        for r in range(N):
            for c in range(N):
                if (r, c) in check:
                    continue

                check.add((r, c))
                queue[head] = [r, c]
                rear += 1
                start = head
                people = countries[r][c]

                while head < rear:
                    # 여기서 위 반복문과 똑같은 r, c 변수를 사용해서 오류가 났었다
                    # 해결하기 위해 qr, qc 라는 변수명으로 변경하여 사용
                    qr, qc = queue[head]
                    head += 1
                    for i in range(4):
                        nr = qr + dr[i]
                        nc = qc + dc[i]

                        if nr < 0 or nr >= N or nc < 0 or nc >= N:
                            continue

                        if (nr, nc) in check:
                            continue

                        if L <= abs(countries[qr][qc] - countries[nr][nc]) <= R:
                            check.add((nr, nc))
                            people += countries[nr][nc]
                            queue[rear] = [nr, nc]
                            rear += 1
                            is_change = True

                for ele in queue[start:rear]:
                    tr, tc = ele
                    countries[tr][tc] = people // (rear - start)

        if not is_change:
            return answer - 1


N, L, R = map(int, input().split())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
countries = []
for _ in range(N):
    countries.append(list(map(int, sys.stdin.readline().split())))

print(moving())
