def solution(sentence):
    stack = []
    open = ('(', '[')
    close = (')', ']')
    for ele in sentence:
        if ele in open:
            stack.append(ele)
            continue
        if ele in close:
            if not stack:
                return 'no'
            if open.index(stack[-1]) == close.index(ele):
                stack.pop()
                continue
            else:
                return 'no'
    if stack:
        return 'no'
    return 'yes'


while True:
    sentence = list(input())
    if sentence == ['.']:
        break
    print(solution(sentence))
