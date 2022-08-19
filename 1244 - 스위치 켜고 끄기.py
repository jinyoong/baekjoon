N = int(input())
switch_lst = [0] + list(map(int, input().split()))
M = int(input())
students = [list(map(int, input().split())) for _ in range(M)]


def solution():

    for student in students:
        gender, number = student

        if gender == 2:

            start = end = number
            switch_lst[number] = (switch_lst[number] + 1) % 2

            while True:

                start -= 1
                end += 1

                if start < 1 or end >= N + 1:
                    break

                if switch_lst[start] != switch_lst[end]:
                    break

                switch_lst[start] = switch_lst[end] = (switch_lst[start] + 1) % 2

        else:

            for k in range(number, N + 1, number):
                switch_lst[k] = (switch_lst[k] + 1) % 2

    return switch_lst[1:]


answer = solution()

for i in range(0, N, 20):
    print(*answer[i:i+20])
