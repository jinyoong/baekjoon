N, M = map(int, input().split())
set_s = [input() for _ in range(N)]
target_lst = [input() for _ in range(M)]

answer = 0
trie = set()

for s in set_s:
    temp = ''
    for alpha in s:
        temp += alpha
        if temp not in trie:
            trie.add(temp)

for target in target_lst:
    if target in trie:
        answer += 1

# for target in target_lst:
#     length = len(target)
#
#     for s in set_s:
#         if target == s[:length]:
#             answer += 1
#             break
#
#
print(answer)

