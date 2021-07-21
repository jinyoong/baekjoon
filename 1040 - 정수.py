# n, k = map(str, input().split())
# diff_ct = 0
# num_list = []
# if k == '1':
#     if int(n[0]) <= int(n[1]):
#         print(str(int(n[0])+1) * len(n))
#     else:
#         print(str(int(n[0])) * len(n))
# elif int(k) == len(n):
#     a = int(n)
#     while True:
#         a += 1
#         if len(set(str(a))) == int(k):
#             print(a)
#             break
# else:
#     for i in range(len(n)-1):
#         if n[i] != n[i+1]:
#             diff_ct += 1
#             num_list.append(int(n[i]))
#         if diff_ct == int(k):
#             num_list.sort()
#             # 바꿔야 하는 뒤에 남아있는 숫자
#             nead_ch = n[i+1:]
#             for num in num_list:
#                 if int(str(num) * len(nead_ch)) > int(nead_ch):
#                     answer = n[:i+1] + str(num)
#                     print(answer)
#                     break
#             else:
#                 temp = int(n[i])
#                 while True:
#                     temp += 1
#                     if int(n[i-1]) != temp:
#                         answer = n[:i] + str(temp) + str(min(num_list)) * len(nead_ch)
#                         print(answer)
#                         break
#             break