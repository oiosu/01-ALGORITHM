# 출력은 표준 출력을 사용한다. 
# 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 
# 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다. 

T = int(input()) #테스트케이스 
PS_list = list(input()) #괄호 리스트 
result = 0  #result : 괄호 쌍이 맞는지

for i in range(PS_list):
    if i == '(':
        result += 1
    elif i == ')':
        result = 1
    if result < 0 : #괄호 쌍이 맞지 않아 괄호가 남는 경우 
        print('NO') #no 출력하고
        break #break 해준다. 
    if result > 0: #모두 반복하고 쌍이 맞지 않는 경우 
        print('NO') #no 출력
    elif result == 0: #쌍이 맞는 경우 
        print('YES') #yes 출력