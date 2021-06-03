croatia_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

s = input()
answer = 0

for c_alpha in croatia_alpha:

    if s == '':
        break
    else:
        if c_alpha in s:
            answer += s.count(c_alpha)
            s = s.replace(c_alpha, ' ')
        else:
            pass
answer = answer + len(s) - s.count(' ')
print(answer)