def virus(linked_lst):
    answer = -1  # 1은 빼고 세야 하니까 -1부터
    visited = [0] * (com_num + 1)  # 이미 한 번 지나간 컴퓨터
    link_stack = [1]  # 찾아볼 컴퓨터
    while link_stack:
        temp = link_stack.pop(0)
        visited[temp] = 1
        if len(linked_lst[temp]) == 1 and linked_lst[temp] == temp:  # 현재 번호와 연결된 컴퓨터에서 연결된 컴퓨터가 현재 번호 컴퓨터밖에 없는 경우
            continue
        for ele in linked_lst[temp]:  # 현재 번호 컴퓨터에서 갈 수 있는 컴퓨터 찾기
            if not visited[ele] and ele not in link_stack:  # 이미 지나온 컴퓨터이거나, 찾아볼 컴퓨터로 추가되지 않은 경우는 넘어감
                link_stack.append(ele)
    for i in visited:
        if i:
            answer += 1
    return answer


for _ in range(1):
    com_num = int(input())
    link_cnt = int(input())
    linked_lst = [[] for _ in range(com_num + 1)]
    for _ in range(link_cnt):  # 인접 리스트 만들기
        a, b = map(int, input().split())
        if b not in linked_lst[a]:
            linked_lst[a].append(b)
        if a not in linked_lst[a]:
            linked_lst[b].append(a)
    print(virus(linked_lst))
