import sys

# 최소 숫자를 만들기 위한 미리 계산된 값 (n ≤ 10일 때)
min_digits = ["", "", "1", "7", "4", "2", "6", "8", "10", "18", "22"]

# 최소 숫자 구하기
def get_min_number(n):
    if n <= 10:
        return min_digits[n]
    q, r = divmod(n - 2, 7)
    return min_digits[r + 2] + "8" * q

# 최대 숫자 구하기
def get_max_number(n):
    if n % 2 == 0:
        # n이 짝수일 경우
        result = "1" * (n // 2)  # '1'을 n//2개 만큼 반복하여 result에 저장
    else:
        # n이 홀수일 경우
        result = "7"  # '7'을 앞에 추가
        result += "1" * (n // 2 - 1)  # 나머지 부분은 '1'을 (n//2 - 1)번 반복하여 추가
    return result

# 입력 처리
t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    print(get_min_number(n), get_max_number(n))
