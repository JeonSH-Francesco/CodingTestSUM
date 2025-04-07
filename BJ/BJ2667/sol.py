#입력 : 지도의 크기 N(정사각형)
N = int(input())

#지도 정보 입력(0:집 없음, 1: 집 있음)
arr=[list(map(int,input())) for _ in range(N)]

#방문 여부를 저장할 2차원 리스트 (0:미방문, 1:방문)
v=[[0]*N for _ in range(N)]

#단지 내 집의 수를 저장할 리스트
ans=[]

#BFS함수 : 시작 좌표 (si,sj)부터 연결된 모든 집을 탐색
def bfs(si,sj):
    q=[]
    q.append((si,sj))
    v[si][sj]=1
    cnt=1 #집 개수 구하는 변수
    
    #큐가 빌 때까지 반복
    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            #조건: 범위 내, 미 방문, 집(1)인 경우
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]==1 and v[ni][nj]==0:
                q.append((ni,nj)) #큐에 추가
                v[ni][nj]=1 #방문 표시
                cnt+=1 #집의 개수 증가
    return cnt #연결된 집의 총 수 반환


for i in range(N):
    for j in range(N):
        #아직 방문하지 않은 집이 있을 경우 BFS 실행
        if arr[i][j]==1 and v[i][j]==0:
            ans.append(bfs(i,j)) #탐색 결과를 리스트에 추가
            
#결과 출력
ans.sort() #오름 차순 정렬
print(len(ans)) # 총 단지 수 출력
print(*ans,sep='\n') # 각 단지의 집 수 출력


'''
https://www.acmicpc.net/problem/2667


7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
3
7
8
9

'''
