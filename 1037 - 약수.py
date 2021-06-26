T = int(input())

yak_lst = list(map(int, input().split()))

yak_lst.sort()

print(yak_lst[0] * yak_lst[-1])