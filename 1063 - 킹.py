alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
directions = {'R': (0, 1), 'L': (0, -1), 'B': (1, 0), 'T': (-1, 0),
              'RT': (-1, 1), 'LT': (-1, -1), 'RB': (1, 1), 'LB': (1, -1)}

k, s, n = input().split()
move_list = [input() for _ in range(int(n))]

king = [8-int(k[1]), alpha.index(k[0])]
stone = [8-int(s[1]), alpha.index(s[0])]


def location(king, stone, move):
    king_r, king_c = king
    stone_r, stone_c = stone
    move_r, move_c = directions[move]

    king_nr, king_nc = king_r + move_r, king_c + move_c
    stone_nr, stone_nc = stone_r + move_r, stone_c + move_c

    if king_nr < 0 or king_nr >= 8 or king_nc < 0 or king_nc >= 8:
        return king, stone

    if [king_nr, king_nc] != stone:
        return [king_nr, king_nc], stone

    if stone_nr < 0 or stone_nr >= 8 or stone_nc < 0 or stone_nc >= 8:
        return king, stone

    return [king_nr, king_nc], [stone_nr, stone_nc]


for m in move_list:
    king, stone = location(king, stone, m)

answer = [alpha[king[1]]+str(8-king[0]), alpha[stone[1]]+str(8-stone[0])]

for ans in answer:
    print(ans)
