a, b = map(str, input().split())
list_a = []
temp = ''
for i in range(-1, -len(a) - 1, -1):
    temp += a[i]
    if i % 3 == 0:
        list_a.insert(0, int(temp[::-1]))
        temp = ''
    if temp and i == -len(a):
        list_a.insert(0, int(temp[::-1]))

list_b = []
temp = ''
for i in range(-1, -len(b) - 1, -1):
    temp += b[i]
    if i % 3 == 0:
        list_b.insert(0, int(temp[::-1]))
        temp = ''
    if temp and i == -len(b):
        list_b.insert(0, int(temp[::-1]))
print(list_a, list_b)

print(a + b)