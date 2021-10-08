n = int(input())

cards = [i+1 for i in range(n)]

start = 1  # 현재 카드의 맨 위를 찾기 위한 변수
end = 0  # 현재 카드의 맨 뒤
cnt = n - 1

while True:
    start %= n
    end %= n

    if not cards[start]:  # 카드가 나올 때까지
        start += 1
        continue

    cards[end] = cards[start]  # 카드의 맨 밑으로 맨 위 카드를 옮김

    cnt -= 1

    if cnt <= 0:  # 만약 다 돌았으면 출력
        print(cards[end])
        break

    cards[start] = 0  # 맨 위를 0으로 표시
    start += 2  # 한 사이클은 맨 위 카드 버리고, 그 다음 맨 위 카드를 맨 끝으로 옮기는 거니까 시작 위치를 2 더해줌
    end += 1
