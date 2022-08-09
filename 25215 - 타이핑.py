typing = input()


def solution():
    answer = 0
    is_up = False

    for i in range(len(typing)):
        answer += 1

        if i == len(typing) - 1:
            if (is_up and typing[i].islower()) or (not is_up and typing[i].isupper()):
                answer += 1
            return answer

        if is_up and typing[i].islower():  # 대문자가 활성화된 상태이면서 소문자를 입력해야 하는 경우
            if typing[i + 1].islower():  # 소문자가 연속해서 2개라면 마름모를 누르는게 낫고, 아니라면 별을 누르는게 낫다
                is_up = False
            answer += 1

        if not is_up and typing[i].isupper():
            if typing[i + 1].isupper():
                is_up = True
            answer += 1


print(solution())
