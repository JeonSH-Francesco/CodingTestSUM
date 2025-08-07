import heapq
import sys

INF = float('inf')  # 무한대 값을 정의합니다. 도달 불가능한 경로를 나타낼 때 사용합니다.
MAX_N = 2000  # 코드트리 랜드의 최대 도시 개수입니다.
MAX_ID = 30005  # 여행상품 ID의 최대값입니다. (문제 제약 조건에 따라 30000까지 가능하므로 여유 있게 설정)

# 입력을 빠르게 받기 위한 설정입니다.
input = sys.stdin.readline

N, M = 0, 0  # 도시의 개수 N과 간선의 개수 M을 초기화합니다.
A = []  # 코드트리 랜드의 간선 정보를 인접 행렬로 저장합니다. A[u][v]는 u에서 v로 가는 간선의 가중치입니다.
D = []  # 다익스트라 알고리즘을 통해 현재 시작 도시로부터 각 도시까지의 최단 경로를 저장합니다.
isMade = [] # 여행상품 ID가 이전에 생성된 적이 있는지 여부를 저장합니다.
isCancel = []  # 여행상품 ID가 취소되었거나 이미 판매되었는지 여부를 저장합니다.
S = 0  # 여행 상품의 현재 출발지 도시 번호입니다. 초기값은 0번 도시입니다.

# 여행 상품(Package) 정보를 저장하고 우선순위 비교를 위한 클래스입니다.
class Package:
    def __init__(self, id, revenue, dest, profit):
        self.id = id         # 고유 식별자 ID
        self.revenue = revenue # 이 상품을 판매하여 얻는 매출
        self.dest = dest     # 이 상품의 도착 도시
        self.profit = profit # 여행사가 이 상품을 판매하여 얻는 순수익 (매출 - 최단 거리 비용)
        
    # 우선순위 큐(heapq)에서 Package 객체들을 비교하기 위한 메서드입니다.
    # heapq는 기본적으로 최소 힙이므로, 최대 힙처럼 동작하게 하려면 비교 로직을 반대로 정의합니다.
    # 1. profit이 클수록 우선순위가 높습니다.
    # 2. profit이 같다면, id가 작을수록 우선순위가 높습니다.
    def __lt__(self, other):
        if self.profit == other.profit:
            return self.id < other.id  # profit이 같으면 id가 작은 순으로 (최소 힙이므로 <)
        return self.profit > other.profit  # profit이 클수록 우선 순위 높게 (최소 힙이므로 >)

pq = []  # 판매 대기 중인 여행 상품들을 저장하는 우선순위 큐입니다.

# dijkstra 알고리즘을 통해 현재 시작 도시 S에서 각 도시로 가는 최단 거리를 구합니다.
# 인접 행렬 기반의 O(N^2) 다익스트라 구현입니다.
def dijkstra():
    global D
    D = [INF] * N  # 모든 도시까지의 최단 거리를 무한대로 초기화합니다.
    visit = [False] * N  # 각 도시의 방문 여부를 기록합니다.
    D[S] = 0  # 시작 도시 S에서 S까지의 거리는 0입니다.
    
    # N번 반복하여 N개의 도시를 모두 방문합니다.
    for _ in range(N):
        v = -1  # 현재까지 방문하지 않은 도시 중 최단 거리가 가장 짧은 도시를 찾습니다.
        minDist = INF
        for j in range(N):
            if not visit[j] and minDist > D[j]:
                v = j
                minDist = D[j]
        
        # 더 이상 방문할 수 있는 도시가 없으면 종료합니다.
        if v == -1:
            break
        
        visit[v] = True  # 해당 도시를 방문 처리합니다.
        
        # 선택된 도시 v를 경유하여 다른 도시로 가는 최단 거리를 갱신합니다.
        for j in range(N):
            # v에서 j로 가는 간선이 존재하고, v를 경유하는 것이 더 짧은 경로라면 갱신합니다.
            if A[v][j] != INF and D[j] > D[v] + A[v][j]:
                D[j] = D[v] + A[v][j]

# 명령어 100: 코드트리 랜드 건설
# 주어진 코드트리 랜드 정보를 인접 행렬 A에 저장합니다.
def buildLand(n_param, m_param, arr):
    global A, N, M
    N, M = n_param, m_param
    A = [[INF]*N for _ in range(N)]  # 인접 행렬을 무한대로 초기화합니다.
    for i in range(N):
        A[i][i] = 0  # 자기 자신에게 가는 비용은 0입니다.
    
    # 주어진 M개의 간선 정보를 인접 행렬에 저장합니다.
    for i in range(M):
        u, v, w = arr[i*3], arr[i*3+1], arr[i*3+2]
        # 양방향 간선이므로 A[u][v]와 A[v][u] 모두 업데이트합니다.
        # 두 도시 사이에 여러 간선이 주어질 수 있으므로, 최소 가중치를 저장합니다.
        A[u][v] = min(A[u][v], w)
        A[v][u] = min(A[v][u], w)

# 명령어 200: 여행 상품 생성
# 새로운 여행 상품을 생성하고 우선순위 큐에 추가합니다.
def addPackage(id, revenue, dest):
    global isMade, pq
    isMade[id] = True  # 해당 ID의 상품이 생성되었음을 기록합니다.
    
    # 도착지까지 도달 불가능한 경우 profit을 음수로 설정하여 판매 불가 처리합니다.
    # D[dest]가 INF인 경우, profit은 -INF가 됩니다.
    profit = revenue - D[dest]
    
    # Package 객체를 생성하고 우선순위 큐에 추가합니다.
    heapq.heappush(pq, Package(id, revenue, dest, profit))

# 명령어 300: 여행 상품 취소
# id에 해당하는 여행 상품이 취소되었음을 기록합니다.
def cancelPackage(id):
    global isCancel
    # 만들어진 적 있는 여행 상품에 대해서만 취소할 수 있습니다.
    if isMade[id]:
        isCancel[id] = True  # 해당 ID의 상품이 취소되었음을 표시합니다.

# 명령어 400: 최적의 여행 상품 판매
# 관리 목록에서 조건에 맞는 최적의 여행 상품을 선택하여 판매합니다.
def sellPackage():
    global pq, isCancel
    while pq:  # 우선순위 큐가 비어있지 않은 동안 반복합니다.
        p = pq[0]  # 큐의 최상단(가장 우선순위 높은) 상품을 미리 확인합니다.
        
        # 현재 최적이라고 판단된 상품의 이득이 0보다 작다면,
        # 우선순위 큐의 특성상 그 뒤의 모든 상품도 이득이 0보다 작거나 같으므로
        # 더 이상 판매 가능한 상품이 없다고 판단하고 반복을 종료합니다.
        if p.profit < 0:
            break
        
        # 큐에서 실제로 상품을 제거합니다.
        heapq.heappop(pq)
        
        # 제거된 상품이 이전에 취소되었거나 이미 판매된 상품이 아니라면,
        # 이 상품이 현재 판매 가능한 최적의 상품입니다.
        if not isCancel[p.id]:
            isCancel[p.id] = True  # 이 상품이 판매되었음을 표시하여 중복 판매를 방지합니다.
            return p.id  # 판매된 상품의 ID를 반환합니다.
            
    return -1  # 판매 가능한 상품이 전혀 없는 경우 -1을 반환합니다.

# 명령어 500: 여행 상품의 출발지 변경
# 여행 상품의 출발지를 s로 변경하고, 이에 따라 모든 상품의 profit을 재계산합니다.
def changeStart(param):
    global S, pq
    S = param  # 출발지를 새로운 값으로 갱신합니다.
    dijkstra()  # 새로운 출발지에 대해 모든 도시까지의 최단 거리를 다시 계산합니다.
    
    temp_packages = []
    # 기존의 우선순위 큐에 있는 모든 상품들을 임시 리스트로 옮깁니다.
    # 이 과정에서 큐는 비워집니다.
    while pq:
        temp_packages.append(heapq.heappop(pq))
        
    # 임시 리스트에 있던 각 상품에 대해 새로운 최단 거리를 기반으로 profit을 재계산하고,
    # 이를 다시 우선순위 큐에 추가합니다. 이렇게 하면 큐가 새로운 profit 기준으로 재정렬됩니다.
    for p in temp_packages:
        # D[p.dest]가 INF인 경우, profit은 -INF가 됩니다.
        p.profit = p.revenue - D[p.dest]
        heapq.heappush(pq, p)

# 메인 실행 로직입니다.
def main():
    global isCancel, isMade
    Q = int(input())  # 총 명령의 수 Q를 입력받습니다.
    
    # 여행 상품의 생성 및 취소/판매 상태를 기록하는 배열을 초기화합니다.
    isMade = [False] * MAX_ID 
    isCancel = [False] * MAX_ID  
    
    # 총 Q개의 쿼리를 순서대로 입력받아 처리합니다.
    for _ in range(Q):
        query = list(map(int, input().split()))
        T = query[0]  # 명령의 종류를 나타내는 코드입니다.
        
        # 명령 코드에 따라 적절한 함수를 호출하여 처리합니다.
        if T == 100:
            # 100번 명령: 코드트리 랜드 건설
            # N, M, 그리고 M개의 간선 정보를 전달합니다.
            buildLand(query[1], query[2], query[3:])
            dijkstra() # 초기 출발지(0번 도시)에 대해 최단 거리를 계산합니다.
        elif T == 200:
            # 200번 명령: 여행 상품 생성
            id, revenue, dest = query[1], query[2], query[3]
            addPackage(id, revenue, dest)
        elif T == 300:
            # 300번 명령: 여행 상품 취소
            id = query[1]
            cancelPackage(id)
        elif T == 400:
            # 400번 명령: 최적의 여행 상품 판매
            # 판매된 상품의 ID를 출력합니다. 판매할 상품이 없으면 -1을 출력합니다.
            print(sellPackage())
        elif T == 500:
            # 500번 명령: 여행 상품의 출발지 변경
            changeStart(query[1])

# 스크립트가 직접 실행될 때 main 함수를 호출합니다.
if __name__ == "__main__":
    main()
