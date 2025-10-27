def solution(numbers):
    #정수 리스트를 문자 리스트로 변환
    numbers=list(map(str,numbers))
    
    # 두 문자열을 이어붙인 결과를 비교해 내림차순 정렬
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    # 정렬된 숫자들을 이어붙임
    answer=''.join(numbers)
    
    return '0' if answer[0]=='0' else answer
