a = input()

num = [i for i in range(10)]
calc = ['+', '-']

a_num = []
a_calc = []

temp = ''
for i in a:
    if i in calc:
        a_num.append(int(temp))
        a_calc.append(i)
        temp = ''
    else:
        temp += i
a_num.append(int(temp))

# print(a_num)
# print(a_calc)

for i in range(len(a_calc)-1):
    if a_calc[i] == '-' and a_calc[i + 1] == '+':
        a_calc[i + 1] = '-'

# print(a_calc)

sum_num = a_num[0]

for k in range(1, len(a_num)):
    if a_calc[k - 1] == '-':
        sum_num -= a_num[k]
    else:
        sum_num += a_num[k]

print(sum_num)
