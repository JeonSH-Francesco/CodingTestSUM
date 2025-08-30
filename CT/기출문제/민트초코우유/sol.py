from collections import deque
N, T = map(int,input().split()) # 배열 NxN 크기, T는 턴의 수
raw_MCT = [list(input()) for _ in range(N)]

#100이 민트, 010이 초코, 001이 우유가 되도록 하기 위함
MINT, CHOCO, MILK = 1,2,4
MCT = [[0]*N for _ in range(N)]

#배열 입력
for i in range(N):
    for j in range(N):
        if raw_MCT[i][j]=='T':
            MCT[i][j]=MINT # 1로 세팅
        elif raw_MCT[i][j]=='C':
            MCT[i][j]=CHOCO # 2로 세팅
        else:
            MCT[i][j]=MILK # 4로 세팅
#신앙심
B=[list(map(int,input().split())) for _ in range(N)]

#방향
dxs, dys= [-1,1,0,0,], [0,0,-1,1]

def in_range(x,y):
    return 0<=x<N and 0<=y<N

'''
아침
    모든 학생의 B가 1씩 증가
'''
def morning():
    for i in range(N):
        for j in range(N):
            B[i][j]+=1



'''
점심
    2차원 격자에서의 Flood Fill
        대표자 선정을 곁들인 (신앙심 큼, 행 작, 열 작)
        신앙심 재조정 (대표자 : cnt-1만큼 증가, 나머지는 1씩 감소)
'''
def flood_fill(visited,i,j):
    visited[i][j]=True #시작 좌표 방문 표시
    B[i][j]-=1 # 대표자 후보를 포함한 그룹원은 신앙심 1 감소
    q=deque([(i,j)]) #BFS 큐에 시작점 넣기
    cnt=1 #그룹 크기 (현재 좌표 포함이므로 1부터 시작)

    px, py = i,j #현재 대표자 후보 좌표 (기본은 시작점)
    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx+dx, cy+dy

            #격자 안, 미방문, 같은 음식 취향이라면 그룹에 포함
            if in_range(nx,ny) and not visited[nx][ny] and MCT[cx][cy]==MCT[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny]=True
                B[nx][ny]-=1 #그룹원이므로 신앙심 1 감소
                cnt+=1 #그룹 크기 +1

                #대표자 후보 갱신 기준 (신앙심 큰, 행 번호 작, 열 번호 작)
                origin_cr = (B[px][py], -px, -py)
                new_cr = (B[nx][ny],-nx,-ny)
                if origin_cr <new_cr:
                    px, py = nx, ny
                    
    #대표자는 그룹 크기만큼 신앙심을 추가로 얻음
    B[px][py] +=cnt
    return (px,py) #대표자의 좌표 반환

def afternoon():
    #대표자 리스트
    rep_list=[]
    visited=[[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                rep=flood_fill(visited,i,j)
                rep_list.append(rep)
    #그룹 내 대표자들 반환
    return rep_list

'''
저녁
    신앙심 전파 순서 : 민초우/ 민초 초우 민우/ 민초우 (같은 그룹내에선 신앙심 큼, 행 작, 열 작)
    신앙심 전파
    -> 방향 전파 (B%4=> 위,아래,왼,오)
    -> 간절함 얻기 (간절함 : B-1, B>=1)
    방향 대로 1칸씩 전진(방어상태에 있는 친구는 안함)
        간절함이 0이 되거나, 격자 밖이면 조기종료
        대상자에게 강한전파/ 약한 전파가 있다.
    
    강한 전파 : x>y 
    ->대상자의 취향이 완전 바뀜(전파자의 것으로)
    ->전파자의 간절함 -(y+1)
    ->대상자의 신앙심 +1
    
    약한 전파 : x<=y 
    ->전파자의 취향이 대상자의 취향과 결합됨.(상태 관리를 bitmask로 할래)
    ->전파자의 간절함 : 0
    ->대상자의 신앙심 x 만큼 증가
    대상자는 방어상태가 된다.
'''
def spread(x,y,d,plz,defense):
    nx, ny = x, y
    while True:
        nx, ny = nx+dxs[d], ny+dys[d]

        if plz<=0 or not in_range(nx,ny):
            break
        #같은 음식을 좋아하는 것을 필터
        if MCT[x][y]==MCT[nx][ny]:
            continue
        
        #강한 전파
        if plz>B[nx][ny]:
            MCT[nx][ny]=MCT[x][y]
            plz-=B[nx][ny]+1
            B[nx][ny]+=1
            defense[nx][ny]=True

        #약한 전파
        else:
            MCT[nx][ny]= MCT[nx][ny] | MCT[x][y]
            B[nx][ny]+=plz
            plz=0
            defense[nx][ny]=True

def evening(rep_list):
    defense = [[False]*N for _ in range(N)]
    def get_criteria(p):
        x,y = p
        #신앙심 전파 순서 : 민초우/ 민초 초우 민우/ 민초우 (같은 그룹내에선 신앙심 큼, 행 작, 열 작)
        rank_mapper = {1:1, 2:1, 4:1, 3:2, 5:2, 6:2, 7:3}
        #신앙심 오름차순, 행, 열 순
        return (rank_mapper[MCT[x][y]],-B[x][y],x,y)
        
    #정렬 됨.
    rep_list =sorted(rep_list,key=get_criteria)
    
    for x,y in rep_list: #모든 대표자 좌표 (x,y)에 대해
        if defense[x][y]: #방어 상태면 (전파 못 받게 차단된 상태이면)
            continue #건너 뜀
        d = B[x][y] %4 # 전파할 방향 (신앙심 %4-> 0:상, 1:하, 2:좌, 3:우)
        plz = B[x][y]-1 #간절함= 현재 신앙심-1
        B[x][y]=1 #대표자는 전파 후 신앙심을 1로 리셋
        
        #전파 실행
        spread(x,y,d,plz,defense)

'''
출력
    민초우,민초,민우,초우,우,초,민 순으로 신앙심 총 합 출력
'''
def print_all():
    #cnt는 비트마스크 취향별 신앙심 총합 계산을 위한 배열
    cnt=[0]*8
    
    #cnt[k]는 취향 조합 k번 그룹의 신앙심 총합
    for i in range(N):
        for j in range(N):
            cnt[MCT[i][j]] +=B[i][j]

    print(cnt[MINT|CHOCO|MILK], cnt[MINT|CHOCO], cnt[MINT|MILK], cnt[CHOCO|MILK],cnt[MILK], cnt[CHOCO], cnt[MINT])
            

for _ in range(T):
    morning()
    rep_list = afternoon()
    evening(rep_list)
    print_all()


'''


4 2
TTCC
TTTM
CCMM
CMMM
1 3 3 3
2 23 16 8
12 6 7 8
12 8 3 5


33 0 0 14 17 31 7
35 9 0 1 10 21 4

'''
