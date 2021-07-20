temp_b = 2000
d_price = []

for i in range(5):
    if i <= 2:
        b_price = int(input())
        if b_price <= temp_b:
            temp_b = b_price
    else:
        drink = int(input())
        d_price.append(drink)

print(temp_b + min(d_price) - 50)