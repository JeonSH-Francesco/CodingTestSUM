def dfs(index, computers, visited):
    visited[index] = True  # 현재 컴퓨터를 방문했다고 표시
    for i in range(len(computers)):
        if computers[index][i] == 1 and not visited[i]:  # 연결된 컴퓨터가 아직 방문되지 않았으면
            dfs(i, computers, visited)  # 그 컴퓨터에 대해 재귀적으로 DFS 호출

def solution(n, computers):
    visited = [False] * n  # 모든 컴퓨터가 방문되지 않은 상태로 초기화
    network_count = 0  # 네트워크의 수
    
    for i in range(n):
        if not visited[i]:  # 아직 방문하지 않은 컴퓨터가 있으면
            dfs(i, computers, visited)  # 해당 컴퓨터에서 DFS 시작
            network_count += 1  # 새로운 네트워크가 발견되었으므로 카운트 증가
    
    return network_count


test_case1=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
test_case2=[[1, 1, 0], [1, 1, 1], [0, 1, 1]]

print(solution(3,test_case1))
print(solution(3,test_case2))

'''
def solution(n, computers):
    #방문 여부를 기록할 리스트를 만든다.
    visited =[ ]
    for i in range(n):
        visited.append(False) #모든 컴퓨터는 처음에 방문하지 않았다고 설정한다.
    def dfs(index):
        visited[index]=True
        #현재 컴퓨터와 연결된 다른 컴퓨터들 확인
        for i in range(n):
            #연결된 컴퓨터(i)가 아직 방문하지 않았으면, 재귀적으로 DFS를 호출
            if computers[index][i] == 1 and not visited[i]:
                dfs(i)
                
    network_count =0
    #모든 컴퓨터에 대해서, 방문하지 않은 컴퓨터가 있으면 DFS 시작
    for i in range(n):
        if not visited[i]:
            dfs(i) #해당 컴퓨터에서 DFS를 시작
            network_count +=1
    return network_count

'''
