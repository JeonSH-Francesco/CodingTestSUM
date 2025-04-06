def dfs(c):
    global ans
    v[c]=1
    ans+=1

    for n in arr[c]:
        if not v[n]:
            dfs(n)

N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    s,e = map(int,input().split())
    arr[s].append(e)
    arr[e].append(s)

v=[0]*(N+1)
ans=0
dfs(1)
result = ans-1

print(result)

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
