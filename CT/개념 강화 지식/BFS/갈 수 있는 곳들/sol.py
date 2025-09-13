from collections import deque

n, k =map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]
points = [tuple(map(int,input().split())) for _ in range(k)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

dxy=[(-1,0),(1,0),(0,-1),(0,1)]

def bfs():
    q=deque()
    visited=[[False]*n for _ in range(n)]
    
    for r, c in points:
        x,y = r-1, c-1
        if grid[x][y]==0 and not visited[x][y]:
            visited[x][y]=True
            q.append((x,y))
    cnt=0
    
    while q:
        x,y = q.popleft()
        cnt+=1
        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            if in_range(nx,ny) and not visited[nx][ny] and grid[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny]=True
                
    return cnt

print(bfs())
            
            
'''
3 2
0 0 0
0 0 1
1 0 0
1 1
1 2

->7


4 2
0 1 0 0
0 1 0 0
0 1 1 1
0 1 0 0
1 4
4 4

->6
'''
