#너비 우선 탐색을 통해 (0,0)->(N-1,M-1)까지의 최소 이동 칸 수를 구하는 함수
def bfs(si,sj,ei,ej):
    q=[] #BFS에서 사용할 큐
    v=[[0]*M for _ in range(N)] #방문 여부와 최단 거리 기록을 위한 2차원 배열
    
    q.append((si,sj)) #시작 좌표를 큐에 삽입
    v[si][sj]=1 # 시작 좌표 방문 표시 (1부터 시작하여 칸 수 포함)
    
    while q: #큐가 빌 때까지 반복
        ci, cj = q.pop(0) #현재 위치 꺼냄(FIFO)
        #도착점에 도달하면 해당 위치의 값(v[ei][ej]) 반환 -> 이동한 칸 수
        if(ci, cj) ==(ei, ej):
            return v[ei][ej]
        
        #4방향(상,하,좌,우), 범위내, 조건에 맞으면 : arr==1, v==0
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj #다음 위치 계산
            
            #범위 안에 있고, 이동 가능한 길이며, 아직 방문하지 않은 경우
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]==1 and v[ni][nj]==0:
                q.append((ni,nj)) #큐에 다음 위치 추가
                v[ni][nj] = v[ci][cj]+1 #현재 위치 값+1 해서 거리 기록
                
#------입력 처리------        
N, M = map(int, input().split()) #N : 행수, M : 열 수
arr=[list(map(int,input())) for _ in range(N)] #미로 정보 입력

#------BFS 실행 ------
ans = bfs(0, 0, N-1, M-1)  # (0,0)부터 (N-1,M-1)까지 최단 거리 계산
print(ans)  # 결과 출력
'''
https://www.acmicpc.net/problem/2178
4 6
101111
101010
101011
111011
15
'''
