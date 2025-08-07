import heapq

class PriorityQueue:
    def __init__(self): # 빈 Priority Queue 하나를 생성합니다.
        self.items = []

    def push(self, item): # 우선순위 큐에 데이터를 추가합니다.
        heapq.heappush(self.items, -item)

    def pop(self):  # 우선순위 큐에 있는 데이터 중 최댓값에 해당하는 데이터를 반환하고 제거합니다.
        if self.empty():
            return -1
        return -heapq.heappop(self.items)

    def top(self): # 우선순위 큐에 있는 데이터 중 최댓값에 해당하는 데이터를 제거하지 않고 반환합니다.
        if self.empty():
            return -1
        return -self.items[0]

    def size(self): # 우선순위 큐에 있는 데이터 수를 반환합니다.
        return len(self.items)

    def empty(self):  # 우선순위 큐가 비어있으면 True를 반환합니다.
        return 1 if not self.items else 0


# 입력 처리
N = int(input())
pq = PriorityQueue()

for _ in range(N):
    line = input().split()
    cmd = line[0]

    if cmd == "push":
        pq.push(int(line[1]))
    elif cmd == "pop":
        print(pq.pop())
    elif cmd == "top":
        print(pq.top())
    elif cmd == "size":
        print(pq.size())
    elif cmd == "empty":
        print(pq.empty())

'''
입력1)

6
push 3
size
empty
pop
push 3
size

출력1)

1
0
3
1

입력2)

12
push 1
push 2
top
size
empty
pop
pop
size
empty
push 3
empty
top

출력2)

2
2
0
2
1
0
1
0
3
'''
