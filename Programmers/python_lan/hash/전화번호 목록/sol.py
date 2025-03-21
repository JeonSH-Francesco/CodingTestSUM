def solution(phone_book):
    phone_book.sort()  # 문자열 정렬 (사전순 정렬로 인해 접두어 관계 확인이 쉬워짐)
    
    for a, b in zip(phone_book, phone_book[1:]):
        if b.startswith(a):  # 앞 번호가 뒷 번호의 접두사인지 확인
            return False
        
    return True

# 테스트 케이스들
test_cases = [
    ["119", "97674223", "1195524421"],
    ["123", "456", "789"],
    ["12", "123", "1235", "567", "88"],
]

# 각 테스트 케이스 실행 및 결과 출력
for phone_book in test_cases:
    result = solution(phone_book)
    print(result)
