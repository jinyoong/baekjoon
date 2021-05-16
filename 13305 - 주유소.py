count_city = int(input())

road_len = list(map(int, input().split()))

city_price = list(map(int, input().split()))

oil_price = city_price[0]

answer = 0
road = 0

for i in range(1, len(city_price)):
    road += road_len[i - 1]
    if i == len(city_price) - 1:
        answer += road * oil_price
    elif city_price[i] <= oil_price:
        # print(city_price[i])
        answer += road * oil_price
        oil_price = city_price[i]
        road = 0

print(answer)
