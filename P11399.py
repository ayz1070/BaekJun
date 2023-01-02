n = int(input())

time = list(map(int,input().split()))

time.sort()
"""
num = 0
sum = 0

for t in time:
    num = num + t
    sum = sum + num
print(sum)
"""
tot = 0
for i in range(0,n+1):
    tot += sum(time[0:i])

print(tot)
