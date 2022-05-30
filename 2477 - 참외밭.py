K = int(input())

length_lst = [0, 0, 0, 0, 0, 0]
distance_lst = [0, 0, 0, 0, 0, 0]
answer = 0

for i in range(6):
    distance, length = map(int, input().split())

    distance_lst[i] = distance
    length_lst[i] = length

start_idx = 0

for i in range(6):
    # 가장 긴 변 2개를 이루는 방향은 항상 연속해서 한 번씩만 나오게 되어있다.
    d1, d2 = distance_lst[i], distance_lst[(i + 1) % 6]
    if distance_lst.count(d1) == 1 and distance_lst.count(d2) == 1:
        start_idx = i

original_area = length_lst[start_idx] * length_lst[(start_idx + 1) % 6]
diff_area = length_lst[(start_idx + 3) % 6] * length_lst[(start_idx + 4) % 6]

print(int(original_area - diff_area) * K)

"""
7
3 30
1 60
3 20
1 100
4 50
2 160

7
1 60
3 20
1 100
4 50
2 160
3 30

7
1 100
4 50
2 160
3 30
1 60
3 20

1
3 60
2 20
3 100
1 50
4 160
2 30

1
3 60
1 20
4 160
2 50
3 100
1 30
"""