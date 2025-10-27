def solution(citations):
    citations.sort(reverse=True)  # 인용 횟수를 내림차순 정렬
    for i, c in enumerate(citations):
        if i + 1 > c:  # i는 0부터 시작하므로 i+1편의 논문이 i+1회 이상 인용된 건지 확인
            return i
    return len(citations)
