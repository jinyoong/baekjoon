T = int(input())

# parenthesis : 괄호
answer = []

for i in range(T):
    input_str = list(input())
    temp = []

    for j in range(len(input_str)):
        # print('현재 {}인덱스인 {}를 봅니다.'.format(j, input_str[j]))
        if not temp:
            temp.append(input_str[j])
        else:
            if input_str[j] == ')' and temp[-1] == '(':
                temp.pop()
            else:
                temp.append(input_str[j])
    # print(input_str)
    # print(temp)
    if not temp:
        answer.append('YES')
    else:
        answer.append('NO')

for ans in answer:
    print(ans)
