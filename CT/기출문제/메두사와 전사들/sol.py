'''
NxN 맵
    -0 based
    -도로 0/ 도로 1

메두사
    -(S_r,S_c) -> (E_r,E_c)
    -최단 경로로 이동
    -도로만 이동

전사
    -M명
    -i번 전사 : (r_i,c_i)
    -메두사를 향해 최단 경로로 이동(도로/비도로 모두 이용)
'''
from collections import deque



#-----------------------------
#범위 체크 함수
def in_range(r,c):
    return 0<=r<N and 0<=c<N
#-----------------------------
#맨헤튼 거리 계산 함수
def manhattan(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])


#-----------------------------
#입력
N, M = map(int,input().split()) # N은 격자 크기, M은 전사의 수

V= list(map(int,input().split())) # 메두사의 시작 좌표, 공원(목적지)의 좌표를 추출하기 위한 임시 list
S, E =(V[0],V[1]), (V[2],V[3]) # list V에 대하여 좌표 추출

Warr= list(map(int,input().split())) # 전사의 좌표 추출을 위한 임시 list
W=[[0]*N for _ in range(N)] #전사의 좌표를 저장하기 위한 배열
for i in range(M):
    x,y =Warr[2*i], Warr[2*i+1] #홀수 좌표와 짝수 좌표를 각 쌍으로 해서 전사 좌표를 추출
    W[x][y]+=1 #w전사 표시

A=[list(map(int,input().split())) for _ in range(N)] #도로 정보의 상태를 저장하기 위한 배열
#-----------------------------


dxy1=[(-1,0),(1,0),(0,-1),(0,1)] #상,하,좌,우
dxy2=[(0,-1),(0,1),(-1,0),(1,0)] #좌,우,상,하

#메두사의 도착지점인 공원으로부터 최단 거리가 담긴 배열을 반환하는 함수
def get_dist_from(x,y):
    q=deque()
    res= [[N*N]*N for _ in range(N)] #거리를 나타내는 배열->N*N으로 초기화
    visited=[[False]*N for _ in range(N)] #방문 여부->False로 초기화
    
    q.append((x,y))
    res[x][y]=0 #출발 위치 거리 = 0 
    visited[x][y]=True
    
    while q:
        cx, cy = q.popleft()
        for dx, dy in dxy1:
            nx, ny = cx+ dx, cy+dy
            if in_range(nx,ny) and not visited[nx][ny] and A[nx][ny]==0:
                q.append((nx,ny))
                res[nx][ny] = res[cx][cy]+1
                visited[nx][ny]=True
    return res



#메두사의 이동->dist_from_park에서 얻은 res 맵을 토대로 min_dist를 계속 갱신하면서 다음 좌표(nx,ny) 반환  
'''
[1] 메두사의 이동(위에서 불 가능한 것을 필터링 함)
- 도로를 따라 한 칸 이동(공원까지 최단 경로)
-> 우선순위 : 상하좌우
-> 공원에 도착하면 0출력하고 종료
- 이동한 위치에 있는 전사는 사라짐
- [0]번 이동 불가한 케이스의 경우 -1 출력
'''
def move_medusa(dist_from_park,x,y):
    min_dist = N*N
    X, Y = None , None
    
    for dx, dy in dxy1:
        nx, ny = x+dx, y+dy
        if in_range(nx,ny) and dist_from_park[nx][ny] < min_dist:
            min_dist=dist_from_park[nx][ny]
            X,Y = nx, ny
    return X, Y

#메두사의 시선
'''
[2] 메두사의 시선===> 돌이 된 전사의 수
- 가장 많이 볼 수 있는 방향으로 바라봄 (우선순위 : 상하좌우) 중 한 방향으로 시선
- 시선에 들어온 전사는 해당 턴은 움직이지 않음
'''
def get_scanned_map(x,y,dxy):
    ScanA=[[0]*N for _ in range(N)] #메두사의 시선이 닿으면 1, 닿지 않으면 0
    
    scanned_queue = deque()#전사가 없다고 가정했을 때의 메두사의 시선
    scanned_warrior_queue = deque()# 전사의 위치가 초기에 들어가고, 가려지는 위치를 위한 시선

    #(x,y,t)에서 type을 토대로 /0번 타입 : 왼쪽, 아래/ 1번 타입 : 아래 /2번 타입 : 오른쪽, 아래로만 이동
    for idx, (dx,dy) in enumerate(dxy):
        nx, ny = x + dx, y+dy
        if in_range(nx,ny):
            scanned_queue.append((nx,ny,idx))
            ScanA[nx][ny] = 1 #스캔 된 것이다.
            if W[nx][ny] > 0:
                scanned_warrior_queue.append((nx,ny,idx))
    #0->0,1을 사용 가능하고, 1->1만, 2->1,2만 사용 가능
    while scanned_queue:
        cx, cy, t = scanned_queue.popleft()
        for idx, (dx,dy) in enumerate(dxy):
            if (t,idx) not in [(0,0),(0,1),(1,1),(2,1),(2,2)]:
                continue
            nx, ny = cx+dx, cy+dy
            #중복 제거
            if not in_range(nx,ny) or ScanA[nx][ny]==1:
                continue
            scanned_queue.append((nx,ny,t))
            ScanA[nx][ny]=1
            if W[nx][ny] >0:
                scanned_warrior_queue.append((nx,ny,t))
                
    while scanned_warrior_queue:
        cx, cy, t = scanned_warrior_queue.popleft()
        for idx, (dx,dy) in enumerate(dxy):
            if (t,idx) not in [(0,0),(0,1),(1,1),(2,1),(2,2)]:
                continue
            nx, ny = cx+dx, cy+dy
            #중복 제거
            if not in_range(nx,ny) or ScanA[nx][ny]==0:
                continue
            scanned_warrior_queue.append((nx,ny,t))
            #메두사의 시선 이후 전사에 의해서 다른 전사가 돌로 변하지 않는 경우 처리
            ScanA[nx][ny]=0
            
    cnt=0
    
    for i in range(N):
        for j in range(N):
            if ScanA[i][j]== 1:
                cnt+=W[i][j]
    
    
    return ScanA, cnt

#전사의 이동->
'''
[3] 전사의 이동===> 이동 합
- 돌로 변하지 않는 전사들만 이동
- 메두사를 향해 최대 2칸 이동함.
- 이동 규칙 : 
    - 메두사와의 거리가 줄어드는 방향으로 한 칸 이동(1차 : 상하좌우 /2차 : 좌우상하)
    - 격자 밖 X, 메두사의 시야 X
'''
def move_warrior(sx,sy,ex,ey,scanned_map,dxy):
    #origin_dist = abs(sx-ex)+abs(sy-ey)
    origin_dist = manhattan((sx,sy),(ex,ey))
    for dx, dy in dxy:
        nx, ny = sx +dx, sy+dy
        #if문이 길어질 것 같으므로 not 활용
        if not in_range(nx,ny) or scanned_map[nx][ny]==1:
            continue
        #우선 순위에 따라서 더 가까워 지는 경우가 있는 경우에는
        if manhattan((nx,ny),(ex,ey)) < origin_dist:
            return (nx,ny)
        
        # if abs(nx-ex) + abs(ny-ey) < origin_dist:
        #     return (nx,ny)
    return (sx,sy)

'''[4] 전사의 공격===> 공격 한 전사의 수
- 메두사와 같은 칸의 전사 -> 사라짐
'''

def main():
    
    global S
    '''
    구현 : 공원으로부터 최단거리 BFS를 활용
    [0] 메두사가 공원까지 가는 경로가 없으면 -> -1 출력 / 종료
    '''
    dist_from_park=get_dist_from(E[0],E[1])
    
    # for d in dist_from_park:
    #     print(*d)
    
    if dist_from_park[S[0]][S[1]]==N*N:
        print(-1)
        return
    
    while True:
            #[1] 메두사의 이동
            S= move_medusa(dist_from_park,S[0],S[1])
            #print(S)
            if S==E:
                print(0)
                return
            
            W[S[0]][S[1]]=0
            
            
            #[2] 메두사의 시선
            dxys=[
                [(-1,-1,),(-1,0),(-1,1)],   #상
                [(1,-1),(1,0),(1,1)],       #하
                [(-1,-1),(0,-1),(1,-1)],    #좌
                [(-1,1),(0,1),(1,1)]        #우
            ]   
            #각각 상,하,좌,우에 대해서 메두사가 바라봤을 때의 맵과 전사의 수를 반환하도록 함.
            
            max_scanned_map, max_scanned= None, -1
            for dxy in dxys:
                scanned_map, scanned = get_scanned_map(S[0],S[1],dxy) #메두사의 위치에서 dxy 방향으로 바라봤을 때의 map을 반환
                #바라봤을 때의 전사의 수가 가장 많은 쪽으로의 map을 가져오겠다.
                if scanned > max_scanned: 
                    max_scanned_map = scanned_map
                    max_scanned = scanned
                #print(scanned)
                # for d in scanned_map:
                #     print(*d)
                # print()

            #[3]. 전사의 이동
            next_map = [[0]*N for _ in range(N)]
            #map에서 전사들이 움직일 때, 탐색하면서 하다 보면 움직인 결과에 의해 또 다시 탐색되서 움직이기 때문에 temp배열을 하나 만들어서
            #각 칸에 움직이는 전사들의 좌표를 배열에다 저장 후 복사를 하는 방식으로 해야 함에 주의
            
            move_dist=0
            
            for i in range(N):
                for j in range(N):
                    #시선에 안 걸린 전사만 이동-> 같은 칸에 전사 여러명 있을 수 있음
                    if W[i][j]==0:
                        continue
                    #메두사의 시선이 없는 경우
                    if max_scanned_map[i][j]==0:
                        x,y = i,j
                        for dxy in (dxy1,dxy2):
                            nx, ny = move_warrior(x,y,S[0],S[1],max_scanned_map,dxy)#(x,y)에 있는 전사를 이동
                            if (x,y) !=(nx,ny): #전사가 움직이거나 시선에 의해 막히거나 움직이지 못할 경우 
                                
                                move_dist+=W[i][j]#전사의 수 만큼 더해줘야 함.
                                x,y = nx, ny
                                
                        next_map[x][y] +=W[i][j] #next_map에 현재 위치에 해당하는 전사의 수 만큼 
                    else:
                        #메두사의 시선이 있어 이동하지 못하는 경우 원래 맵에 있던 전사의 수 만큼 더해서 계산
                        next_map[i][j] +=W[i][j]
            
            #원래 맵에다가 next_map으로 옮기는 방식으로 구현
            for i in range(N):
                for j in range(N):
                    W[i][j]=next_map[i][j]
                                
            #[4] 전사의 공격
            attacked_warrior = W[S[0]][S[1]]
            W[S[0]][S[1]]=0
            
            print(move_dist,max_scanned,attacked_warrior)
            
    

main()

'''
4 4
1 3 3 3        
3 1 0 3 1 0 2 2
0 0 0 0        
0 0 0 0        
0 0 1 1
1 0 0 0

'''
