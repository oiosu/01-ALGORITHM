#대문자 문자열만 출력 

n= list(input().split('-'))
ans=''
for i in n:
    ans+=i[0]
print(ans)