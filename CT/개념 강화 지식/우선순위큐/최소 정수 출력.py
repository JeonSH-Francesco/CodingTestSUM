import heapq

n = int(input())  # 연산 수 입력
pq = []  # 최소 힙 (우선순위 큐)

for _ in range(n):
    x = int(input())
    if x == 0:
        if pq:
            print(heapq.heappop(pq))
        else:
            print(0)
    else:
        heapq.heappush(pq, x)

        
'''
8
0
1
324
2346534
5
0
0
0
->


0
1
5
324

-->
연속 출력된 결과
8
0
0
1
324
2346534
5
0
1
0
5
0
324

'''
