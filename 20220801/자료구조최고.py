# 오류가 계속 발생하는 코드 
# 다시 차근차근 문제 풀이할 것!


# n = int(input())
# m = int(input())
# p = True

# for _ in range(m):
#     i = int(input())
#     k = list(map(int, input().split()))
#     for j in range(i-1):
#         if k[j] < k[j+1]: #오름차순 내림차순
#             p = False
#             break
#         if not p: break
# print('Yes' if p else 'No')


# N, M = map(int, input().split())
# chk = True
# for _ in range(M):
#     n = int(input())
#     lst = list(map(int, input().split()))
#     if chk:
#         while len(lst) > 0:
#             tmp = lst.pop()
#             if lst:
#                 if tmp > lst[-1]:
#                     chk = False
#                     break
#                 else:
#                     break
#             if chk:
#                 print('Yes')
#             else:
#                 print('No')
