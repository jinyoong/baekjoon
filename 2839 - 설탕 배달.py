n = int(input())
answer = []

for i in range(n // 5 + 1):
    # print('5킬로그램 설탕은 {}봉지 가져갑니다.'.format(i))
    for j in range((n - 5 * i) // 3 + 1):
        # print('3킬로그램 설탕은 {}봉지 가져갑니다.'.format(j))
        if 5 * i + 3 * j == n:
            # print('5 : {}, 3 : {}'.format(i, j))
            answer.append(i + j)
if not answer:
    print(-1)
else:
    print(min(answer))

# 아래는 진짜 수학 공식을 이용한 것
# 아래 코드로 공부하자

sugar = int(input())

bag = 0
while sugar >= 0:
    if sugar % 5 == 0:  # 5의 배수이면
        bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else:
    print(-1)