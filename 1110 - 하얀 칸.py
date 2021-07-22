result = 0
for i in range(8):
    chess_list = list(input())
    if i % 2 == 0:
        for j in range(0, 8, 2):
            if chess_list[j] == 'F':
                result += 1
    else:
        for j in range(1, 8, 2):
            if chess_list[j] == 'F':
                result += 1

print(result)