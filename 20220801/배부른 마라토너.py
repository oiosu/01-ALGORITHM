
# 시간 초과 _ 다시 풀어보기 


n = int(input().rstrip())
a = []
for _ in range(n+n-1):
    a.append(input().rstrip())

dic = {}

for i in range(n):
    dic[a[i]] = dic.get(a[i],0)+1

for i in range(n,len(a)):
    dic[a[i]] = dic.get(a[i],0)-1

for k,v in dic.items():
    if v>0:
        print(k)