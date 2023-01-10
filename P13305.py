n = int(input())

distances = list(map(int,input().split()))
costs = list(map(int,input().split()))

total = 0
j=0

for i in range(0,len(distances)):
    total += costs[j] * distances[i]
    if costs[j] > costs[i+1]:
        j = i+1
           
print(total)
