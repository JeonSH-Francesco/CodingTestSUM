import heapq


n, m = map(int, input().split())
arr = list(map(int, input().split()))

pq = []

for elem in arr:
    heapq.heappush(pq, -elem) # priority queue에 넣어줍니다.
#print(pq)
for _ in range(m):
    max_val = -heapq.heappop(pq) #가장 큰 수
    heapq.heappush(pq,-(max_val-1)) #1을 뺀 후 push

print(-pq[0])

'''
입력

5 4
1 5 4 2 1
출력

3


예제 설명)
처음에 [1, 5, 4, 2, 1] 이 있습니다.
이 중 최대를 골라 1을 빼주면 결과는 [1, 4, 4, 2, 1]이 됩니다. (1회)
이 중 최대를 골라 1을 빼주면 결과는 [1, 3, 4, 2, 1]이 됩니다. (2회)
이 중 최대를 골라 1을 빼주면 결과는 [1, 3, 3, 2, 1]이 됩니다. (3회)
이 중 최대를 골라 1을 빼주면 결과는 [1, 2, 3, 2, 1]이 됩니다. (4회)
따라서 남아있는 숫자들 중 최댓값은 3이 됩니다.

'''
