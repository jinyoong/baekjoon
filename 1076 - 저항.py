def resistance(list_in):
    res_dict = {'black': 0, 'brown': 1, 'red': 2,
                'orange': 3, 'yellow': 4, 'green': 5,
                'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
    result = res_dict[list_in[0]] * 10 + res_dict[list_in[1]]
    result *= 10 ** res_dict[list_in[-1]]
    return result

color_list = []
for i in range(3):
    color = input()
    color_list.append(color)

print(resistance(color_list))