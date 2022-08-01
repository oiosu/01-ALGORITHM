# n개의 데이터를 입력의 역순으로 출력 
# 1 3 5 6 8 
# 8 6 5 3 1

n = int(input())
numbers = list(map(int, input().split()))
numbers.reverse()

for numbers in numbers:
    print(numbers, end=" ")