from collections import deque

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

# 물은 0 빙하는 1
dxy = [(-1,0), (1,0), (0,-1), (0,1)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def melt_cnt(grid):
    visited = [[False]*m for _ in range(n)]
    q = deque()
    to_melt = []

    # 격자의 바깥과 맞닿은 테두리 물 전부를 BFS 시작점으로
    # 좌 테두리 -> (0,0),(1,0),(2,0),(3,0),(4,0),(5,0)
    # 우 테두리 -> (0,6),(1,6),(2,6),(3,6),(4,6),(5,6)
    for i in range(n):
        for j in [0, m-1]:
            if grid[i][j] == 0 and not visited[i][j]:
                q.append((i, j))
                visited[i][j] = True
    # 상 테두리 -> (0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6)
    # 하 테두리 -> (5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6)
    for j in range(m):
        for i in [0, n-1]:
            if grid[i][j] == 0 and not visited[i][j]:
                q.append((i, j))
                visited[i][j] = True
            
    # 바깥 물을 따라 BFS 확장
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not in_range(nx, ny) or visited[nx][ny]:
                continue
            visited[nx][ny] = True
            if grid[nx][ny] == 0:
                q.append((nx, ny))        # 바깥 물 확장
            else:
                to_melt.append((nx, ny))  # 바깥 물과 맞닿은 빙하 -> 이번 턴에 녹음

    # 빙하 녹이기 (중복 좌표 제거 후 처리)
    for x, y in set(to_melt):
        grid[x][y] = 0

    return len(set(to_melt))
            

# 빙하가 전부 녹는데 걸리는 시간과 마지막으로 녹은 빙하의 크기를 공백을 사이에 두고 출력
time = 0
last = 0

while True:
    cnt = melt_cnt(g)
    if cnt == 0:
        break
    last = cnt
    time += 1

print(time, last)

'''
입력

3 3
0 0 0
0 1 0
0 0 0

출력

1 1

예제 2
입력

6 7
0 0 0 0 0 0 0
0 1 1 1 1 0 0
0 1 1 0 1 1 0
0 1 0 1 1 1 0
0 1 1 1 1 1 0
0 0 0 0 0 0 0

출력

2 4
'''
