# 입력으로 주어진 저항의 저항값을 계산하여 첫째 줄에 출력한다.

#방법1
#통과한 코드 
a = input()
b = input()
c = input()
resisters = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3,
             'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7,
             'grey': 8, 'white': 9}
 
print((resisters[a] * 10 + resisters[b]) * (10 ** resisters[c]))

# 방법2 
# 리스트에 색깔을 정의한 후 입력받은 색깔의 인덱스를 저장하여 덧셈과 곱셉을 해준다. 
# 런타임 에러 코드 
# color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

# A = color.index(input())
# B = color.index(input())
# C = color.index(input())

# print(int(str(A) + (B)) * (10**C))