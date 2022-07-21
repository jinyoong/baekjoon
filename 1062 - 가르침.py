from itertools import combinations

alpha = {"a", "n", "t", "i", "c"}
# all_alpha = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#              "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "Z"}
N, K = map(int, input().split())
words = list(set(input()[4:-4]) - alpha for _ in range(N))

if K < 5:
    print(0)

elif K >= 26:
    print(N)

else:
    all_alpha = set()
    for word in words:
        all_alpha = all_alpha.union(word)

    word_combination = combinations(all_alpha, K - 5)

    answer = 0

    for comb in word_combination:
        result = 0

        for ele in words:

            if not ele.difference(set(comb)):
                result += 1

        answer = max(answer, result)

    print(answer)
