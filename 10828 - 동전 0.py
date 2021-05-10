a, b = map(int, input().split(" "))
money_list = []
need_money_ct = 0
for i in range(a):
    money_list.append(int(input()))
money_list.sort(reverse=True)
for money in money_list:
    if money > b:
        pass
    elif b == 0:
        break
    else:
        need_money_ct += b // money
        b = b % money

print(need_money_ct)