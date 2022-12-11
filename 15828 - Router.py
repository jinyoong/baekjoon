import sys

custom_input = sys.stdin.readline

n = int(input())
numbers = []
idx = 0
count = n


while True:

    packet = int(custom_input())

    if packet == -1:

        if idx == len(numbers):
            print("empty")
        else:
            print(*numbers[idx:])
        break

    if packet == 0:
        idx += 1
        count += 1
        continue

    if count:
        numbers.append(packet)
        count -= 1
