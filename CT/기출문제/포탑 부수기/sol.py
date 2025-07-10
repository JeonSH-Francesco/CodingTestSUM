#입력 처리
N, M, K = map(int,input().split()) # N : 행 수, M : 열 수, K : 턴 수
arr= [list(map(int,input().split())) for _ in range(N)] #각 포탑의 공격력
turn = [[0]*M for _ in range(N)] #각 포탑의 마지막 공격 턴 기록

from collections import deque

#레이저 공격(BFS)함수
def bfs(si,sj,ei,ej):
    q=deque()
    v=[[[] for _ in range(M)] for _ in range(N)] #경로를 표시하기 위한 visited
    q.append((si,sj))
    v[si][sj]=(si,sj)
    d=arr[si][sj] #damage
    
    while q:
        ci, cj = q.popleft()
        if (ci,cj)==(ei,ej): #목적지 도착 시
            arr[ei][ej] = max(0,arr[ei][ej] -d) #음수 방지를 위한 max 사용으로 데미지를 입힘. 공격
        
        #되돌아가며 경로상의 포탑들에게 1/2 데미지
            while True:
                ci, cj = v[ci][cj]
                if(ci,cj)==(si,sj):
                    return True #시작점 도달 시 True반환
                arr[ci][cj]=max(0,arr[ci][cj]-d//2)
                fset.add((ci,cj))
                        
        #우선순위 : 우,하,좌,상(미방문, 조건: >0 포탑있꼬)
        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
            ni,nj = (ci+di)%N, (cj+dj)%M #테두리 연결
            if not v[ni][nj] and arr[ni][nj] > 0:
                q.append((ni,nj))
                v[ni][nj]=(ci,cj) #경로 저장
    #목적지를 찾지 못함!!
    return False

def bomb(si,sj,ei,ej):
    d= arr[si][sj]
    arr[ei][ej] = max(0,arr[ei][ej]-d) #전체 피해
    
    #주변 8방향에 1/2 데미지(공격자 제외)
    for di, dj in ((-1, -1), (-1, 0), (-1, 1),
                   (0, -1),         (0, 1),
                   (1, -1),  (1, 0), (1, 1)):
        ni,nj = (ei+di)%N, (ej+dj)%M #테두리 연결
        if(ni,nj)!=(si,sj):
            arr[ni][nj] = max(0,arr[ni][nj]-d//2)
            fset.add((ni,nj)) #정비 제외 대상

#메인 루프: 총 K 턴
for T in range(1,K+1):
    #[1]공격자 선정 : 공격력이 가장 낮은 것을 선택
    mn, mx_turn, si, sj =5001, 0, -1, -1
    #전체를 순회하면서 공격자 선정
    for i in range(N):
        for j in range(M):
            if arr[i][j]<=0:
                continue #포탑이 아니면 무시
            #조건 우선순위 대로 갱신
            # 공격력이 mn보다 낮은 경우
            # /그런 포탑이 2개 이상인 경우-> 가장 최근에 공격한 포탑
            # /그런 포탑이 2개 이상인 경우-> 각 포탑 위치의 행과 열의 합이 가장 큰 포탑
            # /그런 포탑이 2개 이상인 경우-> 각 포탑 위치의 열 값이 가장 큰 포탑이 선정된다.
            if mn > arr[i][j] or \
                (mn == arr[i][j] and mx_turn<turn[i][j]) or \
                (mn == arr[i][j] and mx_turn==turn[i][j] and si+sj < i+j) or \
                (mn ==arr[i][j] and mx_turn==turn[i][j] and si+sj==i+j and sj <j):
                    
                mn, mx_turn, si, sj = arr[i][j], turn[i][j], i, j #si,sj 새로운 공격자  선정
    
    #[2]공격 대상 선정(공격 당할 포탑 선정) & 포탑 부서짐
    mx, mn_turn, ei, ej =0,T, N, M
    #전체를 순회하면서 공격자 선정
    for i in range(N):
        for j in range(M):
            if arr[i][j]<=0:
                continue #포탑이 아니면 무시
            #조건 우선순위 대로 갱신
            # 공격력이 mn보다 낮은 경우
            # /그런 포탑이 2개 이상인 경우-> 가장 최근에 공격한 포탑
            # /그런 포탑이 2개 이상인 경우-> 각 포탑 위치의 행과 열의 합이 가장 큰 포탑
            # /그런 포탑이 2개 이상인 경우-> 각 포탑 위치의 열 값이 가장 큰 포탑이 선정된다.
            if mx < arr[i][j] or \
                (mx == arr[i][j] and mn_turn>turn[i][j]) or \
                (mx == arr[i][j] and mn_turn==turn[i][j] and ei+ej > i+j) or \
                (mx ==arr[i][j] and mn_turn==turn[i][j] and ei+ej==i+j and ej>j):
                    
                mx, mn_turn, ei, ej = arr[i][j], turn[i][j], i, j #ei, ej 공격 대상자 선정

    #[2-1]공격자의 공격력 강화 + 공격 시점 기록
    arr[si][sj] +=(N+M) # 공격력 상승 -> 즉시 반영시 가장 센 포탑이 될 수도 있기 때문에 이 부분에 위치해야 함.
    turn[si][sj]=T #이번 턴에 공격
    
    #공격에 영향을 받은 포탑들 기록
    fset=set()
    fset.add((si,sj))
    fset.add((ei,ej))
    
    #[2-2]레이저 공격 시도(우하좌상 순서로 최단거리이동->BFS), 실패 시 포탄 공격으로 대체
    #bfs가 성공여부에 따라 포탄공격으로 갈 수 있으므로
    if not bfs(si,sj,ei,ej):
        bomb(si,sj,ei,ej)
    
    #[3]포탑 정비(공격에 영향 없는 포탑은 +1)
    for i in range(N):
        for j in range(M):
            if arr[i][j] >0 and (i,j) not in fset:
                arr[i][j] +=1
    #[4] 생존 포탑 개수 확인 : 1개 이하이면 조기 종료
    cnt=N*M
    for lst in arr:
        cnt-=lst.count(0)
    if cnt<=1: #남은 포탑이 1 이하면 종료
        break


#최종 결과 출력 : 가장 강한 포탑의 공격력
print(max(map(max, arr)))
