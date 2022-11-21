p = int(input())
for _ in range(p):
    n,m=map(int,input().split())

    a,b=1,1
    c=1
    while True:
        a,b=b,(a+b)%m
        c+=1
        if a==0 and b==1: 
            break
    print(n,c)
