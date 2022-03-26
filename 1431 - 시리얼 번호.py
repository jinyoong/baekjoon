def sum_digit(target):
    result = 0
    for ele in target:
        try:
            result += int(ele)
        except ValueError:
            continue

    return result


N = int(input())

serials = [input() for _ in range(N)]

answer = sorted(serials, key=lambda x: (len(x), sum_digit(x), x))

for ans in answer:
    print(ans)
