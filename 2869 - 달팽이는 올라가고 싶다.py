a, b, v = map(int, input().split())

# 하루에 총 올라갈 수 있는 거리는 a - b 이다.
# 낮에 정상까지 도달할 수 있으므로 n일이 지난 후 남은 거리가 a 보다 작거나 같다면 하루가 더 필요하지 않고
# 낮에만 추가로 올라가면 도달이 가능하다.
# 2 1 5 로 주어지면 3일째에 올라가고 미끄러지고를 반복해서 3만큼 올라가고 남은 거리가 2인데 이는 낮에만 올라가면 되므로 총 4일

last_length = v - a
day_length = a - b
day = last_length / day_length
# 수식 v - (a - b) * x <= a 를 만족하는 최초 정수 x에 1을 더한 값이 최종적인 답이므로
# 아래처럼 나눈 값이 정수꼴이거나 소수꼴일 경우로 나누어 x를 구해줘야 한다.
if day % 1 == 0:
    print(int(day) + 1)
else:
    print(int(day) + 2)