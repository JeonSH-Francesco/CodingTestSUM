#import sys
#sys.stdin=open("input.txt","r")

N, MM, H, K = map(int, input().split()) # NxN의 격자 세팅, MM은 도망자 명수, H는 나무의 개수, K는 턴수

#도망자 좌표 입력
arr=[]
for _ in range(MM):
    arr.append(list(map(int,input().split())))
    
#나무 좌표 입력 
tree=set()
for _ in range(H):
    i,j=map(int,input().split())
    tree.add((i,j))
    
# 0(좌) 1(우) 2(하) 3(상)
di = [0, 0, 1, -1]
dj = [-1, 1, 0, 0]
opp={0:1,1:0,2:3,3:2} #벽에 부딪힌 경우 반대 방향으로 세팅을 위한 초기화 작업

# 방향  상 우 하 좌 tagger(술래)방향 (바깥으로 돌 때 방향)
tdi = [-1, 0, 1, 0]
tdj = [0, 1, 0, -1]

# mx_cnt : 최대 몇 칸 이동할지의 변수
mx_cnt=1
#cnt : 이미 몇 칸 이동했는지 카운트
cnt=0
#flag: 술래가 두 번씩 주기로 방향 전환하므로 mx_cnt를 증가시키기 위해 쓰는 스위치 변수
flag=0
#val : 술래의 이동이 바깥으로 진행 중인지, 안 쪽으로 진행 중인지 판단하기 위한 변수
val=1

M=(N+1)//2
ti, tj, td = M, M, 0 #술래의 위치는 정 중앙이라 했으므로 (N+1)//2로 좌표 세팅, 술래 방향은 상(0번째 인덱스)으로 세팅

ans=0
for k in range(1,K+1): # K턴만큼 게임 진행
    #[1]도망자의 이동 arr의 길이 만큼 진행
    for i in range(len(arr)): 
       if abs(arr[i][0]-ti)+abs(arr[i][1]-tj)<=3: #술래와의 거리가 3 이하인 경우 이동
            ni,nj=arr[i][0]+di[arr[i][2]], arr[i][1]+dj[arr[i][2]]
            if 1<=ni<=N and 1<=nj<=N: #다음 움직일 좌표가 범위 내인 경우
                if(ni,nj)!=(ti,tj): #술래 체크해서 이동이 가능하다면
                    arr[i][0],arr[i][1]=ni,nj #이동
                   
            else: #다음 움직일 좌표가 범위 밖인 경우-> 방향 반대
                arr[i][2]=opp[arr[i][2]] #반대 방향전환 및 저장
                ni,nj = arr[i][0]+di[arr[i][2]], arr[i][1]+dj[arr[i][2]] # 반대 방향으로 한 칸 이동 좌표 계산
                
                if(ni,nj)!=(ti,tj): #술래 체크해서 이동이 가능하다면
                   arr[i][0],arr[i][1]=ni,nj #이동

    #[2]술래의 이동
    cnt+=1 
    #cnt==mx_cnt인 경우까지 증가시켜주는 것이 목적이고 cnt가 증가되는 동안은 움직이지 않고 
    #움직이기 전의 턴 수 동안은 시야에서 걸리는 도망자만 잡아낸다.
    ti, tj = ti+tdi[td], tj+tdj[td]
    
    #바깥쪽으로 다 돈 경우(즉,(1,1)위치에 도달한 경우) 안 쪽으로 동작하는 달팽이
    if (ti,tj)==(1,1): 
        mx_cnt, cnt, flag, val= N, 1, 1, -1
        td=2 #초기 방향을 아래(하)로 세팅
        
    #중앙으로 돌아온 경우 (즉, 바깥쪽으로나 안쪽으로나 처음으로 돌아온 경우) 세팅
    elif (ti,tj)==(M,M):
        mx_cnt, cnt, flag, val = 1,0,0,1
        td=0 #초기 방향을 위(상)으로 세팅
        
    #방향을 돌기 시작하는 경우
    else:
        if cnt==mx_cnt:
            cnt=0
            td=(td+val)%4 #우, 하, 좌, 상으로 가야 하므로 val을 1로 세팅하고 4로 나눈 나머지로 td를 결정
            #중요!!
            #td가 바깥쪽으로 돌아서 (1,1) 또는 (M,M)으로 도착한 경우 세팅된 td 즉, 각각 하(td=2), 상(td=0)을 기준으로 val만큼 방향 세팅이 있다는 점 유의!!
            if flag==0:
                flag=1
            else:
                flag=0 #두 번에 한 번씩 길이 증가
                mx_cnt+=val
        
    #[3]도망자 잡기(술래자리 포함 : 3칸) : 나무가 없으면 도망자 잡힘!
    # 술래 위치와 앞으로 1칸, 2칸 이동한 좌표 3칸 시야 집합
    tset = set(((ti,tj), (ti+tdi[td],tj+tdj[td]), (ti+tdi[td]*2,tj+tdj[td]*2)))
    
    for i in range(len(arr)-1, -1, -1):  # 리스트 뒤에서부터 앞으로 거꾸로 순회
    # 술래 시야(tset) 안에 도망자가 있고, 그 위치에 나무(tree)가 없으면
        if (arr[i][0], arr[i][1]) in tset and (arr[i][0], arr[i][1]) not in tree:
            arr.pop(i)  # 해당 도망자를 잡아서 리스트에서 제거
            ans += k    # 잡은 턴수(k)를 점수에 더함
    
    #도망자가 없다면 더 이상 점수도 없음
    if not arr:
        break
print(ans)



'''
5 3 1 1
2 4 1
1 4 2
4 2 1
2 4

1

5 3 1 2
2 4 1
1 4 2
4 2 1
2 4

5

5 3 1 2
2 5 1
1 5 2
4 2 1
2 4


2

5 3 1 10
1 1 0
1 5 1
5 1 0
3 3 

18

'''
