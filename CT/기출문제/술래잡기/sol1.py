import sys
sys.stdin = open("input.txt", "r")

#debugging helper function
def debug_print(arr,N,msg=""):
    grid=[[0]*N for i in range(N)]
    
    for x,y,_ in arr:
        grid[x-1][y-1]=1 #1-based(arr)로 입력 받는 것을-> 0-based로 변환해서 계산해줄 것.
    
    if msg:
        print(msg)
    for row in grid:
        print(''.join(map(str,row)))
    print()
    
'''
[1] 도망자 움직임
    술래와 거리가 3 초과라면 움직이지 않음
    방향에 따라 다음위치가 벽이라면 턴
    다음 위치에 술래가 없다면 움직임
'''
def move_runners(arr,ti,tj,N):
    #차례대로 좌,우,하,상 방향
    di=[0,0,1,-1]
    dj=[-1,1,0,0]
    opp={0:1,1:0,2:3,3:2}
    
    for i in range(len(arr)):
        if abs(arr[i][0] - ti) + abs(arr[i][1] - tj) <= 3:
            ni, nj = arr[i][0] + di[arr[i][2]], arr[i][1]+dj[arr[i][2]]
            if 1<=ni<=N and 1<=nj<=N:
                #범위 안에 있는 경우 -> 다음 움직일 좌표에 술래가 없는 경우    
                if (ni,nj)!=(ti,tj):
                    arr[i][0], arr[i][1] =ni, nj
            else:
                #범위 안을 벗어나는 경우 -> 반대 방향으로 세팅 후 다음 움직일 좌표에 술래가 없는 경우  
                arr[i][2]=opp[arr[i][2]]
                ni, nj = arr[i][0] + di[arr[i][2]], arr[i][1]+dj[arr[i][2]]
                if (ni, nj)!=(ti,tj):
                    arr[i][0], arr[i][1] = ni, nj
    return arr
'''
[2] 술래 움직임
    달팽이 모양에 따라 전진 후 후진
    (1,1), (M,M)
'''
def move_tagger(ti,tj,td,cnt,mx_cnt,flag,val,N,M):
    #방향 상,우,하,좌 tagger(술래) 방향 (바깥으로 돌 때 방향)
    tdi=[-1,0,1,0]
    tdj=[0,1,0,-1]
    
    #현재 술래의 위치 (ti,tj)를 기준으로 tdi/j[td] 방향 확인 후 이동
    ti+=tdi[td]
    tj+=tdj[td]
    cnt+=1 
    #cnt!=mx_cnt인 경우 그냥 술래 이동 및 cnt만 증가 시킴
    
    if (ti,tj)==(1,1):
        #초기 방향을 아래(하)로 세팅
        return ti, tj, 2, 1, N, 1, -1
    elif (ti,tj)==(M,M):
        #초기 방향을 위(상)로 세팅
        return ti, tj, 0, 0, 1, 0, 1
    elif cnt==mx_cnt:
        td=(td+val)%4 #방향 전환
        cnt=0 #방향을 바꿨으니 다시 0부터 이동
        
        if flag==0:
            flag=1
        else:
            flag=0
            mx_cnt+=val #두 번을 주기로 방향이 늘어나므로 거리 늘려줌.

    return ti, tj, td, cnt, mx_cnt, flag, val    


'''
0턴 (중앙 시작)=(3,3)
ti, tj, td = 3, 3, 0, cnt=0, mx_cnt=1, flag=0, val=1

1턴 (위로 한칸)
ti, tj, td = 2, 3, 0, cnt=1, mx_cnt=1, flag=1, val=1
cnt==mx_cnt이므로 방향 전환 준비(우)
2턴
ti, tj, td = 2, 4, 1, cnt=1, mx_cnt=1, flag=0, val=1

3턴
ti, tj, td = 3, 4, 2, cnt=1, mx_cnt=2, flag=1, val=1
4턴
ti, tj, td = 4, 4, 2, cnt=2, mx_cnt=2, flag=0, val=1
cnt==mx_cnt이므로 방향 전환 준비(하)

5턴
ti, tj, td = 4, 3, 3, cnt=1, mx_cnt=2, flag=1, val=1
6턴
ti, tj, td = 4, 2, 3, cnt=2, mx_cnt=2, flag=0, val=1
이런 식으로 증가
'''

'''
[3] 도망자 잡기
    술래 위치에서 방향에 따라 3칸 이때 나무는 제외
    점수 획든 (t턴 x 잡힌 도망자의 수)
'''

def catch_runners(arr,ti,tj,td,tree,k):
    #방향 상,우,하,좌 tagger(술래) 방향 (바깥으로 돌 때 방향)
    tdi=[-1,0,1,0]
    tdj=[0,1,0,-1]
    
    tset=set(((ti,tj), (ti+tdi[td],tj+tdj[td]), (ti+tdi[td]*2,tj+tdj[td]*2)))
    score=0
    
    for i in range(len(arr)-1,-1,-1):
        if (arr[i][0], arr[i][1]) in tset and (arr[i][0], arr[i][1]) not in tree:
            arr.pop(i)
            score+=k
    return arr, score

def main():
    N, MM, H, K = map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(MM)]
    tree = set(tuple(map(int,input().split())) for _ in range(H))
    
    M = (N+1)//2
    ti,tj,td = M,M, 0
    #술래의 위치는 정 중앙이라 했으므로 (N+1)//2로 좌표 세팅, 술래 방향은 상(0번째 인덱스)으로 세팅
    mx_cnt, cnt, flag, val = 1, 0, 0, 1
    # mx_cnt : 최대 몇 칸 이동할지의 변수
    # cnt : 이미 몇 칸 이동했는지 카운트
    # flag: 술래가 두 번씩 주기로 방향 전환하므로 mx_cnt를 증가시키기 위해 쓰는 스위치 변수
    # val : 술래의 이동이 바깥으로 진행 중인지, 안 쪽으로 진행 중인지 판단하기 위한 변수
    
    ans = 0
    
    for k in range(1,K+1):
        #[1] 도망자
        arr = move_runners(arr,ti,tj,N)
        #[2] 술래
        ti, tj, td, cnt, mx_cnt, flag, val = move_tagger(ti,tj,td,cnt,mx_cnt,flag,val,N,M)
        #[3] 술래잡기
        arr, score = catch_runners(arr,ti,tj,td,tree,k)
        ans+=score
        
        if not arr:
            break
    print(ans)
    
main()


'''
input.txt ref->

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
