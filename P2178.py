from collections import deque

N, M = map(int, input().split())

# 그래프 초기화
graph = []

for _ in range(N):
  graph.append(list(map(int, input())))

# bfs
def bfs(x, y):
  # 상하좌우 이동
  dx = [-1, 1, 0, 0] 
  dy = [0, 0, -1, 1]

  # deque으로 큐 생성
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    
    # 현재 위치에서 4가지 방향으로 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 좌표에서 벗어나지 않게끔
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      
      # 0이면 진행 불가
      if graph[nx][ny] == 0:
        continue
      
      # 1이면 진행 가능
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  
  # 마지막 값에서 카운트 값을 뽑는다.
  return graph[N-1][M-1]

print(bfs(0, 0))
