import math

def solution(N, V, A):
    """
    N: 도시 개수
    V: 자전거 속도 (1분에 이동 가능한 거리)
    A: 도시 간 거리 리스트, 길이 = N-1
    return: 총 소요 시간 (분)
    """
    total_time = 0
    for dist in A:
        # 각 구간마다 ceil로 올림 처리
        total_time += math.ceil(dist / V)
    return total_time

# Test cases
test_cases = [
    (4, 10, [10, 20, 25]),  # 예상: 6
    (3, 5, [5, 15]),        # 예상: 4 -> 1+3
    (5, 7, [7, 14, 21, 28]),# 예상: 10 -> 1+2+3+4
    (2, 10, [9]),            # 예상: 1 -> 9/10 올림 = 1
]

for i, (N, V, A) in enumerate(test_cases, 1):
    print(f"Test case {i}: {solution(N, V, A)}")

'''
Test case 1: 6
Test case 2: 4
Test case 3: 10
Test case 4: 1
'''
