def need_click(buttons, goal):

    idx = 0
    click = '0'
    goal = '0' + str(goal)

    if len(buttons) == 10:
        return just_pm

    for num in goal[1:]:
        idx += 1

        if click > goal[:idx]:
            for down in range(0, 10):

                if str(down) not in buttons:
                    click += str(down)
                    break
            continue

        if click < goal[:idx]:
            for up in range(9, -1, -1):

                if str(up) not in buttons:
                    click += str(up)
                    break
            continue

        if num not in buttons:
            click += num
            continue
        for i in range(1, 10):
            up = int(num) + i
            down = int(num) - i

            if up >= 10:
                up = 9
            if down < 0:
                down = 0

            if str(up) not in buttons:
                click += str(up)
                break
            elif str(down) not in buttons:
                click += str(down)
                break
        else:
            continue

    cnt = abs(int(click) - int(goal)) + len(str(int(click)))

    if just_pm > cnt:
        return cnt
    else:
        return just_pm


def solution(buttons, goal):
    result = just_pm

    for i in range(0, 500000):
        up = goal + i
        down = goal - i
        if int(down) < 0:
            down = '0'

        for num in str(down):
            if num in buttons:
                break
        else:
            result = len(str(down)) + i
            break

        for num in str(up):
            if num in buttons:
                break
        else:
            result = len(str(up)) + i
            break

    if just_pm < result:
        return just_pm
    return result


goal = int(input())

break_cnt = int(input())

if break_cnt > 0:
    buttons = input().split()
else:
    buttons = []
just_pm = abs(goal - 100)  # +, - 버튼만으로 이동할 때 필요한 횟수


print(need_click(buttons, goal))
print(solution(buttons, goal))


"""
74146
3
1 2 6
정답 : 52

19
6
1 2 3 5 6 8
정답 : 11

9
10
0 1 2 3 4 5 6 7 8 9
정답 : 91

78
9
0 1 2 4 5 6 7 8 9
정답 : 22

10
9
0 1 2 3 4 5 6 7 8
정답 : 2

1555
8
0 1 3 4 5 6 7 9
정답 : 670

836
9
6 9 1 8 3 4 7 2 5
정답 : 736

0
9
1 2 3 4 5 6 7 8 9
정답 : 1

101
0
정답 : 1
"""