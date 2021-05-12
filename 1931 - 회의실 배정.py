a = int(input())
room_list = []
for i in range(a):
    # 우선 시작 시간과 끝나는 시간을 가지는 리스트를 만든다.
    # 그 뒤 room_list 리스트에 추가함으로 2차원 배열 형태로 만든다.
    temp = list(map(int, input().split(" ")))
    room_list.append(temp)
print(room_list)

room_list2 = sorted(room_list, key=lambda x: (x[1], x[0]))
# 끝나는 시간을 기준으로 재정렬해준다.
print(room_list2)

room_count = 1
finish_time = room_list2[0][1]
for j in range(1, len(room_list2)):
    if room_list2[j][0] >= finish_time:
        finish_time = room_list2[j][1]
        room_count += 1
        print(room_list2[j])
print(room_count)
