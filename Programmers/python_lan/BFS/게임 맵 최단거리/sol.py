from collections import deque

#범위 체크 함수
def in_range(x,y,n,m):
    return 0<=x<n and 0<=y<m

#BFS 함수
def solution(maps):
    n, m = len(maps), len(maps[0]) #행, 열의 크기
    visited=[[False]*m for _ in range(n)] #방문 여부 체크 배열
    #상,하,좌,우
    dxy=[(-1,0),(1,0),(0,-1),(0,1)]
    
    #현재 좌표, 거리, 방문 여부 초기화
    q=deque()
    q.append((0,0,1))
    visited[0][0]=True
    
    while q:
        #좌표, 거리
        x,y,dist = q.popleft()
        #좌표 끝에 도달한 경우 거리 반환
        if x==n-1 and y==m-1:
            return dist
        #네 방향에 대하여
        for dx,dy in dxy:
            nx, ny = x+dx, y+dy
            #범위 안, 미 방문, 길인 경우
            if in_range(nx,ny,n,m) and not visited[nx][ny] and maps[nx][ny]==1:
                visited[nx][ny]=True
                q.append((nx,ny,dist+1))
                #q에 다음 좌표와 거리+1 한 값 추가
    #갈 수 없는 경우라면 -1반환
    return -1
        
