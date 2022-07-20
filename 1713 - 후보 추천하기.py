N = int(input())
count = int(input())
numbers = list(map(int, input().split()))

pictures = []
student = {}

for number in numbers:

    if len(pictures) == N:

        if number in pictures:
            student[number] += 1

        else:
            recommend = 1000
            result = 0
            for i in range(N):
                picture = pictures[i]
                if student[picture] < recommend:
                    recommend = student[picture]
                    result = i

            student[pictures[result]] = 0
            pictures.pop(result)
            student[number] = 1
            pictures.append(number)

    else:

        if number in pictures:
            student[number] += 1

        else:
            student[number] = 1
            pictures.append(number)

pictures.sort()
print(*pictures)
