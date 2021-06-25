import sys

T = int(input())

num_list = []

for i in range(T):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()
for i in range(T):
    print(num_list[i])