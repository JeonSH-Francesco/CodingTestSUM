def solution(d, budget):
    # 요청 금액을 오름차순으로 정렬
    d.sort()
    
    total_cost = 0  # 누적 비용
    answer = 0
    
    for price in d:
        total_cost += price  # 누적 합 계산
        if total_cost <= budget:
            answer += 1  # 예산 내에서 지원 가능한 부서 수 증가
        else:
            break  # 예산 초과 시 더 이상 지원할 수 없음
    
    return answer

test_case1=[1,3,2,5,4]
budget1=9

test_case2=[2,2,3,3]
budget2=10

print(solution(test_case1,budget1))
print(solution(test_case2,budget2))
/*
https://school.programmers.co.kr/learn/courses/30/lessons/12982?language=cpp
3
4

*/
