import sys

n = int(sys.stdin.readline())

matrix = [list(map(int, input().split())) for _ in range(n)]

for k in range(0, n):         
    for a in range(0, n):     
        for b in range(0, n): 
            if matrix[a][k]==1 and matrix[k][b]==1:
                matrix[a][b] = 1
"""
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
        if j == n-1:
            print()
"""


for m in matrix:
   print(*m)
