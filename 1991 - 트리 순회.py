N = int(input())

node_dict = {}
preorder_result = ""
inorder_result = ""
postorder_result = ""

for _ in range(N):
    p, c1, c2 = input().split()
    node_dict[p] = [c1, c2]


def order(parent):
    global preorder_result
    global inorder_result
    global postorder_result

    child1 = node_dict[parent][0]
    child2 = node_dict[parent][1]

    preorder_result += parent
    if child1 != ".":
        order(child1)
    inorder_result += parent
    if child2 != ".":
        order(child2)
    postorder_result += parent


order("A")

print(preorder_result)
print(inorder_result)
print(postorder_result)
