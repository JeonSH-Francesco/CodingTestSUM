import sys
input = sys.stdin.readline

N, K = map(int, input().split())
weight = [0] * (N + 1)  # DP배열의 행과 인덱스를 맞추기 위해서 0번째 인덱스 추가
value = [0] * (N + 1)   # DP배열의 행과 인덱스를 맞추기 위해서 0번째 인덱스 추가
for i in range(1, N + 1):
    weight[i], value[i] = map(int, input().split())

# [1]. 2차원 DP
DP = [[0] * (K + 1) for _ in range(N + 1)]  # 행: 물건의 갯수 (0 ~ N) / 열: 가방의 최대용량(0 ~ K)
for cur_object in range(1, N + 1):          # cur_object: 1부터 N까지 증가
    for limit in range(1, K + 1):               # limit: 가방의 최대용량을 1부터 K까지 증가
        # 메인 아이디어
        if weight[cur_object] <= limit:                     # 현재 물건의 무게가 가방의 최대 용량 이하라면
        	# 현재 물건을 안 넣는 경우, 현재 물건의 무게만큼 빼고 현재 물건을 넣은 경우 중 큰 것
            DP[cur_object][limit] = max(DP[cur_object-1][limit], DP[cur_object-1][limit-weight[cur_object]] + value[cur_object])
        else:                                               # 현재 물건의 무게가 가방의 최대 용량 보다 크다면
            DP[cur_object][limit] = DP[cur_object - 1][limit]   # 현재 물건을 넣지 못한다
print(DP[-1][-1])
