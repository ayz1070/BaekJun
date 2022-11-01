c = int(input())

for _ in range(c):
    sum = 0
    count = 0
    num = list(map(int,input().split()))
    for i in range(1,len(num)):
        sum += num[i]
    for k in range(1,len(num)):
        if num[k] >sum/num[0]:
            count +=1
    print("{0:0.3f}%".format(count/num[0]*100))
    
