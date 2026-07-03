def in_range(x,y):
    #보드 범위 안인지 확인
    return 0<=x<5 and 0<=y<5

def dfs(x,y,board,visited,used_reverse):
    #상,하,좌,우
    dxy=[(-1,0),(1,0),(0,-1),(0,1)]

    visited[x][y]=True
    
    current=board[x][y]
    
    #현재까지 방문한 칸의 개수
    count=0
    
    for i in range(5):
        for j in range(5):
            #visited[i][j]=True인 곳 = 방문한 곳
            if visited[i][j]:
                count+=1
                
    max_len=count
    
    #4방향 탐색
    for dx, dy in dxy:
        nx=x+dx
        ny=y+dy
        
        #범위 안에 있지 않고 방문한 것이라면 pass
        if not in_range(nx,ny):
            continue
        if visited[nx][ny]:
            continue
        
        nxt=board[nx][ny]
        
        #사전 순 뒤 알파벳이면 이동 가능
        if nxt>current:
            max_len = max(max_len,dfs(nx,ny,board,visited,used_reverse))
        #사전 순 앞 알파벳이라면, 단 한번만 이동 가능 -> solution함수 부분 시작할 때 False로 설정한 이유
        #알파벳 역순으로 가서 dfs끝날 때까지는 계속 used_reverse는 True    
        elif nxt<current and not used_reverse:
            max_len = max(max_len,dfs(nx,ny,board,visited,True))
            
    # 백트래킹(상태 복구)
    # 현재 칸 탐색을 모두 마쳤으므로
    # 방문 기록을 지워서 부모 호출 상태로 되돌린다.
    # 마치 방문을 열고 들어가서 방안 조사 후 방문을 닫고 나오는 작업
    # 예)
    # A → B → C 탐색 완료
    # C 방문 취소
    # B 방문 취소
    # 이후 A → 다른 경로 탐색이 그래야 가능해진다!!!
    #가장 중요한 핵심 부분
    visited[x][y]=False
        
    #현재 위치에서 만들 수 있는 최장 길이 변환
    return max_len


def solution(board):
    max_value=0
    
    for i in range(5):
        for j in range(5):
            visited=[[False]*5 for _ in range(5)]
            
            max_value = max(max_value, dfs(i,j,board,visited,False))
            
    return max_value



board = [
    ["A","B","T","T","T"],
    ["T","C","D","E","T"],
    ["T","T","T","F","T"],
    ["B","A","H","G","F"],
    ["C","D","E","F","G"]
]

print(solution(board)) #15
