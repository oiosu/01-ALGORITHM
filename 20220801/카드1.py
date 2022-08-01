# 첫째 줄에 버리는 카드들을 순서대로 출력한다. 
# 제일 마지막에는 남게 되는 카드의 번호를 출력한다.
# 입력 : 7
# 출력 : 1 3 5 7 4 2 6

# deque로 문제풀이 
# from collections import deque

# n = int(input())
# queue = deque(range(1, n+1))

# while len(queue) > 1:
#     print(queue.popleft(), end=" ")
#     queue.append(queue.popleft())

# print(queue[0])

#######################################################

# pop과 append 함수를 사용하여 문제풀이 진행하기 
# 카드를 버리고 난 후 카드가 없다면 반복문을 멈출 수 있게 코드 작성하도록 하기 



# 리스트로 구현한 문제 
l = [i for i in range(1, int(input())+1)]
result = []
cnt = 1
while l:
    if cnt % 2 == 0:
        l.append(l[0])
        l.pop(0)
    else:
        result.append(l[0])
        l.pop(0)
    cnt += 1

print(' '.join(map(str, result)))
 