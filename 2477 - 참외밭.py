K = int(input())

length_lst = [0, 0, 0, 0, 0, 0]
distance_lst = [0, 0, 0, 0, 0, 0]
idx = 0
answer = 0

# 참외밭은 ㄱ 모양을 회전한 육각형 모양! ㄷ, ㄹ 모양은 나올 수 없다
for _ in range(6):
    distance, length = map(int, input().split())

    distance_lst[idx] = distance
    length_lst[idx] = length
    idx += 1

start_idx = 0

for idx, value in enumerate(distance_lst):
    if distance_lst.count(value) == 1:
        start_idx = idx
        break

original_area = length_lst[start_idx] * length_lst[(start_idx + 1) % 6]
diff_area = length_lst[(start_idx + 3) % 6] * length_lst[(start_idx + 4) % 6]

print((original_area - diff_area) * K)

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