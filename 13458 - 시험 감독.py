N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())


def solution(students, main_manager, assistant):
    answer = 0

    for student in students:
        answer += 1

        if student > main_manager:
            student -= main_manager

            if student % assistant:
                answer += (student // assistant) + 1
            else:
                answer += student // assistant

    return answer


print(solution(A, B, C))
