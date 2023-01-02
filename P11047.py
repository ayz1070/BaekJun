n,k = map(int,input().split())

coins = list()

for i in range(n):
    a = int(input())
    coins.append(a)

# 그리디하게 접근하기 위해 내림차순으로 리스트 정렬
coins.sort(reverse=True)

count = 0

for coin in coins:
    if k >= coin:
        count += k//coin
        k = k%coin

print(count)
