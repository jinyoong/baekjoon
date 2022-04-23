text = input()
target = input()
text_len = len(text)
target_len = len(target)
check = [0] * text_len

answer = 0
for i in range(text_len - target_len + 1):
    if check[i]:
        continue

    if text[i:i+target_len] == target:
        check[i:i+target_len] = [1] * target_len
        answer += 1

print(answer)
