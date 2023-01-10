s= int(input())

count = 0
total = 0
for i in range(1,s):
    count+=1
    total += i
    if total > s:
        count -= 1
        break
if s == 1 or s== 2:
    count = 1

print(count)
