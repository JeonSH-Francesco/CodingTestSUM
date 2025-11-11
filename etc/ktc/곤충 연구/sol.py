def solution(N, A):
    max_val = max(A)
    # 배열 A에서 가장 큰 힘 값을 구함 (최대공약수 후보 범위 설정용)

    # 특정 최대공약수를 가지는 곤충들의 수를 저장하기 위한 배열
    freq = [0] * (max_val + 1)
    
    # freq[i] = 힘이 i인 곤충이 몇 마리 있는지 기록
    for num in A:
        freq[num] += 1
    #->freq = [0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1]

    # i를 최대공약수 후보로 했을 때, i의 배수인 곤충들을 모두 세어 누적
    for i in range(2, max_val + 1):
        for j in range(i * 2, max_val + 1, i):
            freq[i] += freq[j]
    #->freq배열을 사용함으로써 i보다 큰 j만 접근하므로 값이 덮어씌워지지 않고 중복 접근(배수 관계)을 자연스럽게 커버함 
    #시간 복잡도 : O(max_val log max_val) 수준으로 빠름
    #i를 최대공약수로 하는 곤충이 각각 몇 마리 있는지 기록
    #->freq = [0,0,4,1,2,1,0,1,0,0,1,0,0,0,1]
    
    # 최대공약수가 2 이상인 경우 중에서 가장 많이 참여할 수 있는 곤충 수 선택
    answer = max(freq[2:], default=0)
    # 모두 서로소인 경우-> 즉, 공약수 없는 경우 대비를 위해 default = 0
    #-> freq[2:]=[4,1,2,1,0,1,0,0,1,0,0,0,1]

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
