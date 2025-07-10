# 10*10 격자, 100턴 (10명 이동, 회전, 값 감소 처리): 시간 충분!
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for _ in range(M):
    i, j = map(lambda x:int(x)-1, input().split())
    arr[i][j]-=1            # 사람은 -1 (같은 위치에 여러명 있을 수 있음)

ei,ej=map(lambda x:int(x)-1, input().split())
arr[ei][ej]=-11             # 비상구 -11

def find_square(arr):
    # [1] 비상구와 모든 사람간의 가장짧은 가로 또는 세로거리 구하기 => L
    mn = N
    for i in range(N):
        for j in range(N):
            if -11<arr[i][j]<0:     # 사람인 경우
                mn=min(mn, max(abs(ei-i), abs(ej-j)))

    # [2] (0,0)부터 순회하면서 길이 L인 정사각형에 비상구와 사람있는지 체크 => 리턴 L+1
    for si in range(N-mn):
        for sj in range(N-mn):                  # 가능한 모든 시작위치
            if si<=ei<=si+mn and sj<=ej<=sj+mn: # 비상구가 포함된 사각형!
                for i in range(si, si+mn+1):
                    for j in range(sj, sj+mn+1):
                        if -11<arr[i][j]<0:     # 사람인 경우 리턴!
                            return si,sj,mn+1

def find_exit(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j]==-11:
                return i,j

# K턴 또는 모두탈출까지 모든 사람의 이동거리 누적, 모두 탈출했으면 종료
ans = 0
cnt = M
for _ in range(K):
    # [1] 모든 참가자 (동시에)한 칸 이동(출구 최단거리 방향 상/하 우선)
    # 출구에 도착하면 즉시 탈출
    narr = [x[:] for x in arr]
    for i in range(N):
        for j in range(N):
            if -11<arr[i][j]<0: # 사람인 경우
                dist = abs(ei-i)+abs(ej-j)
                # 네방향(상하우선), 범위내, 벽아니고 <=0, 거리가 dist보다 작으면
                for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ni,nj = i+di, j+dj
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj]<=0 and dist>(abs(ei-ni)+abs(ej-nj)):
                        ans+=arr[i][j]          # 현재 인원수가 이동하는 것이니 이동거리에 누적
                        narr[i][j]-=arr[i][j]   # 이동처리
                        if arr[ni][nj]==-11:    # 비상구인 경우
                            cnt+=arr[i][j]      # 탈출!
                        else:                   # 일반빈칸 또는 사람있는자리
                            narr[ni][nj]+=arr[i][j] # 들어온 인원 추가
                        break
    arr = narr
    if cnt==0:
        break

    # [2] 미로회전(출구와 한 명이상 참가자를 포함하는 가장 작은 정사각형
    # 시계방향 90도: 같은크기->좌상단행열, 내구도 -1
    si,sj,L = find_square(arr)

    narr = [x[:] for x in arr]
    for i in range(L):
        for j in range(L):
            narr[si+i][sj+j]=arr[si+L-1-j][sj+i]
            if narr[si+i][sj+j]>0:      # 벽이면 회전시 1감소
                narr[si+i][sj+j]-=1
    arr = narr
    # 회전으로 달라졌으므로... 비상구 위치 저장
    ei,ej = find_exit(arr)

print(-ans)
print(ei+1,ej+1)
