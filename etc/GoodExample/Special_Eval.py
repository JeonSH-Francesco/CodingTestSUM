from collections import Counter

#계산 방식
def index_score(a, b, c):
    score = 0
    for x, k in Counter([a, b, c]).items():
        score += (int(x) ** k)
    return score

def solution(s1, s2, s3):
    n = len(s1)
    m2 = len(s2)
    m3 = len(s3)

    min_value = -float('inf')
    #dp[i][j][k] = 최대 점수
    dp = [[[min_value] * (m3 + 1) for _ in range(m2 + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 0

    #i : s1의 현재 위치(0~n)
    #j : s2를 몇 글자까지 소비했는가(0~m2)
    #k : s3를 몇 글자까지 소비했는가(0~m3)
    
    for i in range(n):
        for j in range(m2 + 1):
            for k in range(m3 + 1):

                if dp[i][j][k] == min_value:
                    continue

                cur = dp[i][j][k]
                s1c = s1[i]

                # s2 후보 -> 현재 s1[i]에 대응할 s2문자 후보 (문자, 다음 j)
                t2_choices = []
                remaining_s1 = n - i - 1  # 이번 index 이후 남은 s1 자리 수

                if j < m2:
                    t2_choices.append((s2[j], j + 1))  # s2[j] 실제문자 사용, j 증가

                # 삽입 가능 조건은 남은 s1 자리가 남은 s2 문자 수 이상일 때
                if (m2 - j) <= remaining_s1:
                    for d in range(10):
                        t2_choices.append((str(d), j))  # 임의 문자 삽입, j 유지

                # s3 후보 -> 현재 s1[i]에 대응할 s3문자 후보 (문자, 다음 k)
                t3_choices = []

                if k < m3:
                    t3_choices.append((s3[k], k + 1))  # s3[k] 사용

                # 삽입 가능 조건은 남은 s1 자리가 남은 s3 문자 수 이상일 때
                if (m3 - k) <= remaining_s1:
                    for d in range(10):
                        t3_choices.append((str(d), k))  # 임의 문자 삽입, k 유지
                        
                #nj, nk : 선택 후 갱신될 j,k 값
                #sc : 현재 index에서 얻는 점수
                for t2c, nj in t2_choices:
                    for t3c, nk in t3_choices:
                        sc = index_score(s1c, t2c, t3c)
                        
                        if dp[i + 1][nj][nk] < cur + sc:
                            dp[i + 1][nj][nk] = cur + sc
    
    #dp[n][m2][m3] : s1전부, s2전부, s3전부 소비했을 때 최대 점수
    return dp[n][m2][m3]


print(solution("13598", "29", "198"))    # 1454
print(solution("09867", "2967", "057"))  # 1627
print(solution("4321", "1", "1234"))     # 54
print(solution("467", "862", "567"))     # 284
