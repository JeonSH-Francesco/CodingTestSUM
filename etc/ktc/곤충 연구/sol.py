def solution(N, A):
    max_val = max(A)
    # 배열 A에서 가장 큰 힘 값을 구함 (최대공약수 후보 범위 설정용)

    freq = [0] * (max_val + 1)
    for num in A:
        freq[num] += 1
    # freq[i] = 힘이 i인 곤충이 몇 마리 있는지 기록

    # i를 최대공약수 후보로 했을 때, i의 배수인 곤충들을 모두 세어 누적
    for i in range(2, max_val + 1):
        for j in range(i * 2, max_val + 1, i):
            freq[i] += freq[j]

    # 최대공약수가 2 이상인 경우 중에서 가장 많이 참여할 수 있는 곤충 수 선택
    answer = max(freq[2:], default=0)

    # 2마리 이상이어야 연구 가능, 아니면 -1 반환
    return answer if answer >= 2 else -1


# 테스트 케이스
test_cases = [
    (5, [4, 10, 3, 4, 14]),  # 예상: 4 (4,10,4,14)
    (4, [3, 5, 7, 11]),       # 예상: -1 (모든 수 최대공약수 1)
    (6, [6, 12, 18, 24, 6, 30]), # 예상: 6 (모두 최대공약수 6 포함)
    (3, [2, 2, 3]),           # 예상: 2 (2,2)
]

for i, (N, A) in enumerate(test_cases, 1):
    print(f"Test case {i}: {solution(N, A)}")
'''
Test case 1: 4
Test case 2: -1
Test case 3: 6
Test case 4: 2
'''
