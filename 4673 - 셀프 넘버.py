def self_num(n):
    ans = n
    for i in str(n):
        ans += int(i)
    return ans
num_list = [i for i in range(1, 10000)]

for i in range(1, 10001):
    if self_num(i) in num_list:
        num_list.pop(num_list.index(self_num(i)))
for num in num_list:
    print(num)