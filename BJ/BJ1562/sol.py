N = int(input())
MOD = 1_000_000_000

# dp[length][digit][mask] = 길이 length에서 마지막 숫자가 digit이고, mask 상태일 때 경우의 수
dp = [[[0]*1024 for _ in range(10)] for _ in range(N+1)]

# 길이 1인 계단수 초기화 (0으로 시작 X)
for i in range(1, 10):
    dp[1][i][1<<i] = 1

for length in range(1, N):
    for last in range(10):
        for mask in range(1024):
            if dp[length][last][mask] == 0:
                continue
            # 다음 숫자 후보
            for next_digit in [last-1, last+1]:
                if 0 <= next_digit <= 9:
                    next_mask = mask | (1<<next_digit)
                    dp[length+1][next_digit][next_mask] += dp[length][last][mask]
                    dp[length+1][next_digit][next_mask] %= MOD

# 길이 N이고 모든 숫자가 등장한 경우(mask == 0b1111111111 = 1023)
answer = sum(dp[N][digit][1023] for digit in range(10)) % MOD
print(answer)
