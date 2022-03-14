import sys
sys.setrecursionlimit(100000)

numbers = []
answers = []

while True:
    try:
        num = int(input())
        numbers.append(num)
    except:
        break

parent = numbers[0]
nodes = {parent: [-1, -1]}
ancestors = [parent]

for child in numbers[1:]:
    if child < parent:
        nodes[parent][0] = child
        nodes[child] = [-1, -1]
        parent = child
        ancestors += [child]
        continue

    for i in range(len(ancestors)):
        parent = ancestors[i]
        if parent < child:
            nodes[parent][1] = child
            nodes[child] = [-1, -1]
            parent = child
            ancestors = ancestors[:i] + [child]
            break


def post_order(post_parent):
    if nodes[post_parent] == [-1, -1]:
        answers.append(post_parent)
        return

    for i in range(2):
        child = nodes[post_parent][i]
        if child == -1:
            continue
        post_order(child)

    answers.append(post_parent)


post_order(numbers[0])

for ans in answers:
    print(ans)

"""
반례
50
30
45
41
47
98
52
60

50
60
70
80
90
100

50
40
30
20
10
"""