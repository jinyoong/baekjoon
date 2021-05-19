T, M = map(int, input().split())

card_list = list(map(int, input().split()))
card_list.sort(reverse = True)

answer_list = []

for i in range(len(card_list)-2):
   # print('1번째 숫자로 {}를 봅니다.'.format(card_list[i]))
    card_sum = card_list[i]

    for j in range(i+1, len(card_list) - 1):
        # print('2번째 숫자로 {}를 봅니다.'.format(card_list[j]))
        if card_list[i] + card_list[j] <= M:
            card_sum = card_list[i] + card_list[j]

            for k in range(j+1, len(card_list)):
                # print('3번째 숫자로 {}를 봅니다.'.format(card_list[k]))
                if card_list[i] + card_list[j] + card_list[k] <= M:
                    card_sum = card_list[i] + card_list[j] + card_list[k]
                    answer_list.append(card_sum)

print(max(answer_list))