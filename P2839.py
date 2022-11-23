import sys

n = int(sys.stdin.readline())


def sol(n):
    if n>=5 and n!=7 or n==3:
        if n%5==0:  # 나누어 떨어지면 그냥 나눈 값
            count=n//5
        elif n%5==3:    # 나머지가 3이면 5로 나눈 몫에 +1
            count=n//5 +1
        elif n%5==1:    # 나머지가 1이면 한번 덜 나누고 나머지가 6이 됨.
            count=n//5+1
        elif n%5==2:    # 나머지가 2이면 2번 덜 나누고 나머지가 12가 됨.
            count=n//5+2
        elif n%5==4:    # 나머지가 4이면 1번 덜 나누고 나머지가 9가 됨.
            count=n//5+2
    else:
        count = -1
        
    return count

print(sol(n))
