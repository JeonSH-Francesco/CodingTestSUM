def solution(s):
    cnt = 0
    result = []
    
    for char in s:
        if char == ' ':
            cnt = 0
            result.append(' ')
        else:
            # 문자 대소문자 변환을 변수로 처리
            if cnt % 2 == 0:
                converted_char = char.upper()  # 짝수 번째 문자는 대문자
            else:
                converted_char = char.lower()  # 홀수 번째 문자는 소문자
            
            result.append(converted_char)  # 변환된 문자 추가
            cnt += 1
    
    return ''.join(result)

# 테스트 케이스들
test_cases = [
    "try hello world",  # 예시 1
    "hello world",      # 예시 2
    "a b c",            # 예시 3
    "tHis Is a Test",   # 예시 4
    "   multiple spaces",  # 예시 5
]

# 테스트 케이스 출력
for idx, test_case in enumerate(test_cases, 1):
    result = solution(test_case)
    print(f"Test case {idx}: {result}")
