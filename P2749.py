import sys

n = int(sys.stdin.readline())

p = 1500000
# n > 2라면, k(10^n) = 15×10^(n-1)
# k(10^6) = 15 x 10^5 (주기)

def fibo(n):
    a,b=0,1
    for i in range(n):
        a,b=b%1000000,(a+b)%1000000
    return a 
    
print(fibo(n%p))
