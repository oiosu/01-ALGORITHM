# 영학이가 마실 수 있는 우유의 최대 개수를 출력하시오.

n = int(input())
a = list(map(int, input().split()))

count = 0

for i in range(n):
    if a[i] == count % 3:
        count = count + 1

print(count)
