import sys

input = sys.stdin.readline


def heap_push(heap, x):
    idx = len(heap)
    heap.append(x)
    while idx > 1:
        if heap[idx//2] < heap[idx]:
            heap[idx//2], heap[idx] = heap[idx], heap[idx//2]
            idx //= 2
        else:
            break


def heap_pop(heap):
    result = heap[1]
    heap[1], heap[-1] = heap[-1], heap[1]
    heap.pop()
    idx = len(heap)-1
    p = 1

    while p <= idx:
        if p*2+1 <= idx:
            c1, c2 = p*2, p*2+1
            if heap[c1] < heap[c2]:
                c = c2
            else:
                c = c1

            if heap[p] < heap[c]:
                heap[p], heap[c] = heap[c], heap[p]
                p = c
            else:
                break

        elif p*2 <= idx:
            c = p*2

            if heap[p] < heap[c]:
                heap[p], heap[c] = heap[c], heap[p]
                p = c
            else:
                break

        else:
            break

    return result


n = int(input())
presents = [0]
for _ in range(n):
    nums = list(map(int, input().split()))

    if len(nums) == 1:
        if len(presents) == 1:
            print(-1)
        else:
            print(heap_pop(presents))

    else:
        for i in range(1, len(nums)):
            heap_push(presents, nums[i])
