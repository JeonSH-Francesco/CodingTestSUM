K, M = map(int,input().split()) #K는 턴 수, M은 추가로 받는 유물의 수 입력
arr=[list(map(int,input().split())) for _ in range(5)] #5x5의 유적지 입력
lst= list(map(int,input().split())) #추가로 받는 유적을 담기 위한 리스트
ans=[] #답

#90도 시계방향 회전
def rotate(arr,si,sj):
    narr=[x[:] for x in arr]
    for i in range(3):
        for j in range(3):
            narr[si+i][sj+j]=arr[si+3-j-1][sj+i]
    return narr

#bfs를 통해 유물이 있는 경우 탐색
def bfs(arr,v,si,sj,clr):
    q = []
    sset = set() #유물 위치를 저장하기 위한 변수
    cnt = 0 #유물 개수 세기 위한 변수

    q.append((si,sj))
    
    v[si][sj]=1
    sset.add((si,sj))
    cnt+=1
    
    while q:
        ci,cj = q.pop(0)
        # 네방향, 범위내, 미방문, 조건: 같은 값이면
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<5 and 0<=nj<5 and v[ni][nj]==0 and arr[ci][cj]==arr[ni][nj]:
                q.append((ni,nj))
                v[ni][nj]=1
                sset.add((ni,nj))
                cnt+=1

    if cnt>=3:      # 유물로 인정되었고, 제거 모드인 경우(3개 이상인 경우)
        if clr==1:  # 0으로 초기화
            for i,j in sset:
                arr[i][j]=0 #해당 좌표들을 0으로 초기화(제거)
        return cnt #유물이면: cnt 리턴->clr==0인 경우에도 return 함. (이유 : 중요 포인트->if clr==1: indentation이 같은 위치이기에)
    else:#cnt<3인 경우
        return 0 # 3개 미만이면 0리턴
     
#유물이 얼마나 사라지는지 확인
def count_clear(arr, clr):  # clr==1인 경우 3개이상 값들을 0으로 clear
    v = [[0]*5 for _ in range(5)]
    cnt = 0
    for i in range(5):
        for j in range(5):  # 미방문인 경우 같은 값이면 fill
            if v[i][j]==0:
                # 같은 값이면, 3개 이상인 경우
                t = bfs(arr,v,i,j,clr)
                cnt+=t
    return cnt

for _ in range(K):
    #[1]탐사 진행
    mx_cnt=0 #최대 유물 획득 지점 찾기 위한 변수
    #문제 조건에 따라 회전수(90,180,270도 돌리는 것)->열->행 작은 순으로 진행
    for rot in range(1,4): 
        for sj in range(3):
            for si in range(3):
                #rot 회수만큼 90도 시계방향 회전 -> narr
                #arr은 2차원 리스트(5x5정수배열) x[:]는 각 행(1차원 리스트)를 슬라이싱 복사한 것 
                #for x in arr로 각 행에 대해 반복하므로, 전체적으로 2차원 리스트의 복사본을 만든다.
                #deepcopy보다 빠른 이유 : deepcopy는 재귀적으로 모든 자료형의 참조를 확인하고 복사하기에 오버헤드가 큼.
                #반면 x[:]는 리스트 슬라이싱이므로 간단하고 빠르다.
                narr=[x[:]for x in arr] #->이를 통해 탐사마다 회전시키며 최대 유물을 획득할 수 있는 위치,회전 각도를 찾는다.
                for _ in range(rot):
                    narr=rotate(narr,si,sj)
                    
                #가장 많이 나올 수 있는 유물 개수를 cnt해서 선택하기 위한 작업
                t=count_clear(narr,0)
                if mx_cnt<t:
                    mx_cnt=t
                    marr=narr #유물을 최대 개수만큼 할 수 있는 marr를 narr로 갱신
                    
    #유물이 없는 경우 턴 즉시종료
    if mx_cnt==0: #유물이 더 이상 안 나오는 경우
        break #바로 종료
        
    #[2] 연쇄획득
    cnt=0 #실제 턴에서 유물이 얼마나 사라졌는지 계산하기 위한 변수
    arr=marr #최대의 유물을 획득할 수 있는 배열로 갱신
    while True:
        t=count_clear(arr,1)
        if t==0:
            break #연쇄 획득 종료 => 다음 턴으로..
        cnt +=t #발굴한 유물 개수 누적
        
        #arr의 0값인 부분 리스트에서 순서대로 추가
        #문제 조건에 따라 유물을 추가할 경우 열을 기준으로 행 수가 큰 경우가 우선권을 가지므로
        for j in range(5):
            for i in range(4,-1,-1):
                if arr[i][j]==0:
                    arr[i][j]=lst.pop(0)
    ans.append(cnt) #이번턴 연쇄 획득한 개수 추가
    
print(*ans)

'''
2 20
7 6 7 6 7
6 7 6 7 6
6 7 1 5 4
7 6 3 2 1
5 4 3 2 7
3 2 3 5 2 4 6 1 3 2 5 6 2 1 5 6 7 1 2 3
17


'''
