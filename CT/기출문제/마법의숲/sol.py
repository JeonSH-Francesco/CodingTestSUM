R, C, K = map(int,input().split()) #각각 행, 열, 정령의 수
unit = [list(map(int,input().split())) for _ in range(K)] #si, sj, dr

#격자 초기화 : 벽(1) + 빈칸(0)
# 기존 열의 양 옆 1로 세팅/R+3(0,1,2[골렘의 처음 위치 고려한 크기], 마지막 줄)/맨 마지막 행에는 열의 개수+2만큼의 1로 세팅
arr = [[1]+[0]*C+[1] for _ in range(R+3)] +[[1]*(C+2)]
#비상구 위치 저장용 set(정령이 탈출할 수 있는 위치)
exit_set = set()

#상, 우, 하, 좌 (동쪽 : 시계방향) -> dr은 시계방향
di =[-1,0,1,0]
dj =[0,1,0,-1]

#전체 점수 합
ans = 0
num = 2 #골렘 번호(2부터 시작, 0: 미방문, 1: 방문과 겹치지 않기 위함)

#BFS 탐색 : 골렘에 연결된 정령들이 최대 아래로 내려간 행 번호 계산
def bfs(si,sj):
    q=[]
    v=[[0]*(C+2) for _ in range(R+4)]
    mx_i=0 # 정령이 이동한 최하단 행 (출력시 -2해서 리턴)
    
    q.append((si,sj))
    v[si][sj]=1
    
    while q:
        ci, cj = q.pop(0)
        mx_i = max(mx_i,ci)
        
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if v[ni][nj]==0 and  (arr[ci][cj]==arr[ni][nj] or ((ci,cj) in exit_set and arr[ni][nj]>1)):
                q.append((ni,nj))
                v[ni][nj]=1
    return mx_i-2

# 골렘 입력 좌표/방향에 따라서 남쪽이동 및 정령 최대좌표 계산/누적
for cj,dr in unit:
    ci=1 #처음 골렘이 위치하는 행
    
    # [1] 남쪽으로 최대한 이동(남쪽 -> 서쪽 -> 동쪽) 또는 회전하면서 이동
    while True:
        # 남쪽(아래쪽)으로 한칸이동
        if arr[ci+1][cj-1]+arr[ci+2][cj]+arr[ci+1][cj+1]==0:    #  비어있음
            ci+=1
        # 서쪽(왼쪽)으로 회전하면서 아래로 한칸
        elif (arr[ci-1][cj-1]+arr[ci][cj-2]+arr[ci+1][cj-1]+arr[ci+1][cj-2]+arr[ci+2][cj-1])==0:
            ci+=1
            cj-=1
            dr=(dr-1)%4 #출구는 반시계 방향 회전
        # 동쪽(오른쪽)으로 회전하면서 아래로 한칸
        elif (arr[ci-1][cj+1]+arr[ci][cj+2]+arr[ci+1][cj+1]+arr[ci+1][cj+2]+arr[ci+2][cj+1])==0:
            ci+=1
            cj+=1
            dr=(dr+1)%4 #출구는 시계 방향 회전
        #더 이상 이동 불가
        else:
            break #갈 수 없는 경우는 멈춤.
        
    #골렘이 너무 위쪽에 걸쳐 있으면 초기화(배치 실패)
    # 몸이 범위밖(새롭게 탐색시작.. arr등 모두 초기화)
    if ci<4:
        arr = [[1]+[0]*C+[1] for _ in range(R+3)]+[[1]*(C+2)]
        exit_set = set()
        num = 2
    else:
        # [2] 골렘을 맵에 표시 + 비상구위치 추가
        arr[ci+1][cj]=arr[ci-1][cj]=num
        arr[ci][cj-1:cj+2]=[num]*3
        num+=1
        #비상구 위치 추가(현재 방향 기준으로 한 칸 앞)
        exit_set.add((ci+di[dr], cj+dj[dr]))
        ans+=bfs(ci,cj)
        
#정답 출력
print(ans)

'''

6 5 6
2 3
2 0
4 2
2 0
2 0
2 2
29

'''
