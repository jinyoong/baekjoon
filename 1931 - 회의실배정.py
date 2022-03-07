a = int(input())
room_list = []
for i in range(a):

    temp = list(map(int, input().split()))
    room_list.append(temp)

room_list2 = sorted(room_list, key=lambda x: (x[1], x[0]))

room_count = 1
finish_time = room_list2[0][1]

for j in range(1, len(room_list2)):
    if room_list2[j][0] >= finish_time:
        finish_time = room_list2[j][1]
        room_count += 1

print(room_count)
