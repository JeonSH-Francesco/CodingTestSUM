def solution(citations):
    citations.sort(reverse=True)  # 인용 횟수를 내림차순 정렬하여 인덱스=상위 논문 수
    # i+1 = 상위 i+1 편 논문, c=i번째 논문의 인용 횟수
    for i, c in enumerate(citations):
        #상위 h편 논문이 h회 이상 인용되고, 나머지 논문은 h회 이하 인용되면 H-index이므로
        if i + 1 > c:  # i는 0부터 시작하므로 i+1편의 논문이 i+1회 이상 인용된 건지 확인
            return i
    return len(citations)
