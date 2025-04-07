N = int(input())
#N은 컴퓨터의 수
M = int(input())
#M은 간선 수(네트워크 상에 직접 연결되어 있는 컴퓨터의 쌍 수) 

#인접 리스트 생성(컴퓨터 번호는 1번부터 N번까지)
arr=[[] for _ in range(N+1)]

def dfs(c):
    global ans
    v[c]=1
    ans+=1
    
    #현재 컴퓨터 c와 연결된 다른 컴퓨터들을 확인
    for n in arr[c]: 
        if not v[n]: #아직 방문하지 않은(감염되지 않은)컴퓨터라면
            dfs(n) #그 컴퓨터도 감염시키기 위해 DFS 재귀 호출


#네트워크 연결 정보 입력
for _ in range(M):
    s,e = map(int,input().split())
    arr[s].append(e)
    arr[e].append(s) #양방향
    
#방문 여부를 체크할 리스트 초기화
v=[0]*(N+1)
ans=0

dfs(1)

print(ans-1)

'''

https://www.acmicpc.net/problem/2606
7
6
1 2
2 3
1 5
5 2
5 6
4 7
4

'''
