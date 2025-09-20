dis=[-1,0,1,0]
djs=[0,1,0,-1]

#[a,b] / [c,d] 겹치는지 체크 함수
def is_intersect(a:int, b:int, c:int, d:int):
    assert a<=b and c<=d, "Invalid parameter for is_intersect" 
    return not (b<c or d<a)

def sum_area(sum_dp:list[list[int]],si:int,sj:int,ei:int,ej:int)->int:
    assert 1<=si<=ei and 1<=sj<=ej, "Invalid parameter for sum_area"
    return (sum_dp[ei][ej]-sum_dp[ei][sj-1]-sum_dp[si-1][ej]+sum_dp[si-1][sj-1])

class Knight:
    def __init__(self,i:int, j:int, h:int, w:int, power:int)->None:
        self.si:int=i
        self.sj:int=j
        self.h:int=h
        self.w:int=w
        self.power:int=power
        self.total_damage:int=0
    
    #만약 나중에 self.si나 self.h가 바뀌면 self.ei는 같이 갱신되지 않아서 계산이 틀릴 위험이 있기에
    #property(메서드를 마치 변수처럼 쓸 수 있게끔 하는 decorator)를 활용
    @property
    def ei(self)->int:
        return self.si+self.h-1
    
    @property
    def ej(self)->int:
        return self.sj+self.w-1
    
    def is_alive(self)->bool:
        return self.power>0

    #밀리는 것과 관련있는 함수
    #other: direction 밀었을 때, self가 밀리게 되는가
    def is_pushed(self, other:"Knight", direction: int)->bool:
        return (
            is_intersect(
                a=self.si, b=self.ei,
                c=other.si+dis[direction],
                d=other.ei+dis[direction],
            )
            and is_intersect(
                a=self.sj, b=self.ej,
                c=other.sj+djs[direction],
                d=other.ej+djs[direction],
            )
        )

    #self를 direction 방향으로 밀 수 있는가?
    #격자 밖으로 나간다 or 벽이 있다=> false
    def can_move(self, direction:int)->bool:
        global l
        nsi = self.si+dis[direction]
        nei = self.ei+dis[direction]
        nsj = self.sj+djs[direction]
        nej = self.ej+djs[direction]

        if not (1<=nsi and nei<=l and 1<=nsj and nej<=l):
            return False

        #위 좌표에 대하여 벽이 있는지 체크하기 위해서 sum_area 호출해서 벽이 있는 경우=양수인 경우면 false
        if 0< sum_area(
            sum_dp=sum_walls,
            si=nsi,
            sj=nsj,
            ei=nei,
            ej=nej,
        ):
            return False

        return True

    #self 현재 좌표에 있는 가시 수 만큼 데미지 받기
    def desc_power(self)->None:
        num_traps = sum_area(
            sum_dp=sum_traps,
            si=self.si,
            sj=self.sj,
            ei=self.ei,
            ej=self.ej,
        )
        num_traps=min(num_traps,self.power)
        
        self.power-=num_traps
        self.total_damage+=num_traps



l:int =0
n:int=0

#1-based 좌표계
board: list[list[int]]=[]
sum_traps: list[list[int]] = []
sum_walls: list[list[int]] = []

#0-based
knights: list[Knight]=[]

visited: list[bool] = []

def dfs_knight(idx:int, direction:int)->bool:
    global visited,n,knights

    """
    현재 기사 idx를 시작으로, direction 방향으로 연쇄 이동이 가능한지 판별하는 함수
    - 이동 중에 벽이나 체스판 바깥으로 나가면 False
    - 연쇄로 겹치는 기사들도 모두 이동 가능헤야 True
    """
    assert not visited[idx], "Already visited"
    visited[idx]=True

    #idx 기사가 지정된 방향으로 이동할 수 없는 경우
    if not knights[idx].can_move(direction=direction):
        return False

    #아직 방문하지 않은 다른 기사들 중,
    #현재 기사(idx)가 이동했을 때, 겹치게 되는 기사(next_idx)가 있다면 
    for next_idx in range(n):
        #미방문, 살아 있는 경우, idx에 의해 밀려나는 기사라면
        if(
            not visited[next_idx]
            and knights[next_idx].is_alive() 
            and knights[next_idx].is_pushed(
                other=knighs[idx],
                direction=direction
            )
        ):
            #next_idx 기사도 동일 방향으로 연쇄 이동 가능한지 DFS 탐색
            if not dfs_knight(idx=next_idx,direction=direction):
                return False
    return True


def process_move(start_idx:int, direction:int)->None:
    global knights, visited
    
    if not knights[start_idx].is_alive():
        return

    visited=[False]*n
    # dfs를 돌렸을 대, dfs로 기사가 움직일 수 없다면 바로 return
    if not dfs_knight(start_idx, direction=direction):
        return

    for idx in range(n):
        #방문인 경우 그 기사는 밀려야 함.
        if visited[idx]:
            knights[idx].si+=dis[direction]
            knights[idx].sj+=djs[direction]
            
            #데미지를 입은 경우
            if idx!=start_idx and knights[idx].is_alive():
                knights[idx].desc_power()

def read_input():
    global l,n, board,knights, sum_traps,sum_walls

    q:int =0
    l,n,q =map(int,input().split())

    board=[[0]*(l+1) for _ in range(l+1)]
    for i in range(1,l+1):
        line:list[int]=list(map(int,input().split()))
        for j in range(1,l+1):
            board[i][j] = line[j-1]

    knights.clear()
    for _ in range(n):
        i,j,h,w,k = map(int,input().split())
        knight=Knight(i=i,j=j,h=h,w=w,power=k)
        knights.append(knight)

    sum_traps=[[0]*(l+1) for _ in range(l+1)]
    sum_walls=[[0]*(l+1) for _ in range(l+1)]

    # 누적합(1=가시, 2=벽)
    for i in range(1,l+1):
        for j in range(1,l+1):
            sum_traps[i][j]=(
                (1 if board[i][j]==1 else 0)
                + sum_traps[i-1][j]
                + sum_traps[i][j-1]
                - sum_traps[i-1][j-1]
            )
            sum_walls[i][j]=(
                (1 if board[i][j]==2 else 0)
                + sum_walls[i-1][j]
                + sum_walls[i][j-1]
                - sum_walls[i-1][j-1]
            )

    for _ in range(q):
        idx, direction=map(int,input().split())
        #knight의 idx는 0-based
        idx-=1

        process_move(start_idx=idx, direction=direction)

read_input()

answer:int=0
for idx in range(n):
    if knights[idx].is_alive():
        answer +=knights[idx].total_damage
print(answer)

'''
4 3 3
0 0 1 0
0 0 1 0
1 1 0 1
0 0 2 0
1 2 2 1 5
2 1 2 1 1
3 2 1 2 3
1 2
2 1
3 3
->
3

'''
