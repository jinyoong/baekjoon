def max_title(books):
    book_set = list(set(books))
    cnt_lst = []
    for book in book_set:
        cnt_lst.append(books.count(book))

    best = list(zip(book_set, cnt_lst))

    best = sorted(best, key=lambda x: (-x[1], x[0]))

    return best[0][0]


T = int(input())

books = [input() for _ in range(T)]

print(max_title(books))
