from collections import deque

# n행 m열
m,n = map(int,input().split())  

graph = []

# 2차원 행렬 생성
for i in range(n):
    graph.append(list(map(int,input().split())))

queue = deque()

# 1. 그래프에서 1을 찾자
# 2. 1에서 bfs 수행
# 3. 추가 조건 고려
# 3-1. 토마토가 모두 익지 못하면 -1 출력. 즉, 모두 탐색했을 때 0이 존재하면 -1 출력
# 3-2. 이미 모든 토마토가 익어있다면 0을 출력. 고려할 필요 없다. 

# 1. 1(익은 토마토)을 찾자!
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j))

# 그럼 큐에는 1이 담긴 좌표를 담고 있겠지? 확인

# 이동을 위한 요소들
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 2. 1(첫 익은 토마토)에서 bfs 수행
def bfs():
    while queue:
        # 처음 익은 토마토 꺼내자
        x,y = queue.popleft()
        # 상하좌우로 한 칸씩 이동해줘야지.. 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 행렬 범위에서 벗어나지 않는 경우
            if 0<= nx <n and 0<=ny<m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx,ny))

bfs()
res = 0

# 3. 추가 조건
for i in graph:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    # 그래프에서 최댓값을 찾고 1을 빼주면 정답
    res = max(res,max(i))
# 시작을 1로 했으니까 1을 빼줘야지
print(res-1)
    
