def hansoo(n):
    num_list = list(str(n))
    diff_list = []
    for i in range(1, len(num_list)):
        diff_list.append(int(num_list[i]) - int(num_list[i - 1]))
    return len(set(diff_list))

T = int(input())
h_ct = 0

for i in range(1, T + 1):
    if i <= 9:
        h_ct += 1
    else:
        if hansoo(i) == 1:
            h_ct += 1

print(h_ct)