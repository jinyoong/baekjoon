A, B = map(int, input().split())
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

print(len((set_a - set_b).union(set_b - set_a)))
