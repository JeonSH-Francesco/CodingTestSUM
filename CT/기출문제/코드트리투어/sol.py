import heapq

'''

그래프 : 인접 리스트로
여행상품 : Dijkstra로 처리할 것이다.


여행 상품 관리
    상품 객체를 Heap으로 관리
    idTo객체 배열이 필요

    인덱스의 범위가 크면 -> Map
    인덱스의 범위가 작으면 -> 배열


'''

'''
여행 상품 객체
    id, 매출, 비용, 도착지, 삭제 여부
'''
class Package:
    def __init__(self, id_, rev, cost, dest, is_del=False):
        self.id = id_
        self.rev = rev
        self.cost = cost
        self.dest = dest
        self.is_del = is_del

    def __lt__(self, other):
        if self.rev - self.cost == other.rev - other.cost:
            return self.id < other.id
        return self.rev - self.cost > other.rev - other.cost
'''
전역 변수
'''
#초기화
V, E = 0, 0
Graph = []
#heap
packages = []
#사실상 Map은 아니고 배열로 쓸 것
idMap = [None] * 30005
#최단 거리
D = []


'''
ElogV dijkstra
'''
def dijkstra(st):
    global D
    visit = [False] * V
    D = [float("inf")] * V
    D[st] = 0
    q = []
    heapq.heappush(q, (0, st))
    
    while q:
        dist, cur = heapq.heappop(q)
        if visit[cur]:
            continue
        visit[cur] = True

        for dest, d in Graph[cur]:
            if D[dest] > dist + d:
                D[dest] = dist + d
                heapq.heappush(q, (D[dest], dest))
'''
1. 랜드 건설
    도시, 간선 정보가 주어지면 -> 그래프 
    -> 시간 복잡도 : O(간선 개수+ElogV)
    최단 거리 미리 전처리
'''
def build_land(n, m, line):
    global V, E, Graph
    V = n
    E = m
    Graph = [[] for _ in range(V)]
    for i in range(0, E*3, 3):
        s, e, d = line[i], line[i+1], line[i+2]
        Graph[s].append((e, d))
        Graph[e].append((s, d))
    dijkstra(0)
'''
2. 여행 상품 생성
    (id, 매출,비용, 도착지) 여행 상품을 생성
    id는 고유값이며 매출은 revenue(id), 그리고 이 상품의 도착지는 dest(id)입니다. 
    -> 시간 복잡도 : O(logP+비용구하기 ElogV[대략 10000*log2000])(단,P는 상품 개수)인데,
    -> 실제 시간 복잡도 적합한 것은 O(logP+1)
'''
def make_package(id_, rev, dest):
    cost = D[dest]
    new_p = Package(id_, rev, cost, dest)
    heapq.heappush(packages, new_p)
    idMap[new_p.id] = new_p
'''
3. 여행 상품 취소
    id를 갖는 상품이 있다면 삭제
    -> 시간 복잡도 : Lazy Deletion 으로 O(1)로 처리
    Lazy Deletion : 데이터 구조에서 원소를 즉시 삭제하지 않고, 
    "삭제 표시만 해두고 실제 삭제는 나중에 필요할 때 한꺼번에 수행"하는 방식

'''
def cancel_package(id_):
    if idMap[id_] is not None:
        idMap[id_].is_del = True
#heap에서 삭제된 것 은 아니지만 객체에 마킹을 함으로써 Lazy Deletion이 된다.



'''
4. 최적의 상품 의미
    최적의 상품이란?
    매출 -비용이 가장 큰, id가 가장 작은
    만약 매출 -비용이 양수 인 것이 없다면,-1 출력
    있다면 해당 id를 출력하고 관리 상품에서 삭제
    -> 시간 복잡도 : O(logP)
    (Heap 사용을 위해선 매출-비용이 완성된 상태로 관리되어야 함.)
'''
def sell_package():
    candidate = None
    #packages가 남아있는 동안
    while packages:
        candidate = heapq.heappop(packages)
        #가장 높은 우선순위를 뽑아 놓는 과정
        if not candidate.is_del:
            break
        candidate = None
    #candidate가 None이라면 가능한 상품이 없다는 것
    if candidate is None:
        print(-1)
        return
    # 이득을 얻을 수 없어서 판매 안함
    if candidate.rev - candidate.cost < 0:
        heapq.heappush(packages, candidate)
        print(-1)
        return
    #이득을 얻을 수 있음
    print(candidate.id)

'''
5. 출발지 변경
    출발지 변경
    -> 시간 복잡도 : O(1) ? 
    -> Dijkstra 를 사용할 것이므로 O(ElogV)
    최단 거리 전처리 변경
'''
def change_start(s):
    #주의 ! packages라는 힙이 여행상품이 들어있었는데 출발지가 변하는 경우 -> 모든 상품들의 비용이 변한다.
    #packages안에 있는 것들은 사실상 쓸모가 없어지므로 lazy update하는 방법도 있지만,
    #새로 계산을 해서 heap에 넣는 것을 추천 -> heap물갈이
    origin_packages = []
    while packages:
        origin_packages.append(heapq.heappop(packages))
    dijkstra(s)

    for op in origin_packages:
        cost = D[op.dest]
         #cost만 달라짐에 주의!
        new_p = Package(op.id, op.rev, cost, op.dest, op.is_del)
        idMap[new_p.id] = new_p
        heapq.heappush(packages, new_p)

# 메인 시뮬레이션
Q = int(input())
for _ in range(Q):
    cmd, *inp = map(int, input().split())
    if cmd == 100:
        n, m = inp[0], inp[1]
        line = inp[2:]
        build_land(n, m, line)
    elif cmd == 200:
        make_package(*inp)
    elif cmd == 300:
        cancel_package(*inp)
    elif cmd == 400:
        sell_package()
    elif cmd == 500:
        change_start(*inp)

'''
입출력)
16
100 6 7 0 1 3 1 2 2 2 2 1 0 3 5 1 3 3 5 4 1 2 1 3
200 1 5 1
200 2 5 2
200 3 3 1
400
1
400
2
200 4 3 3
200 5 10 5
300 3
400
-1
400
-1
200 6 10 4
500 5
400
5
400
6
400
-1
'''
