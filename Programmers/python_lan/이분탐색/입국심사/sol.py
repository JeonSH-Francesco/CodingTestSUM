def solution(n, times):
    left, right = 1, max(times) * n  # 최대 시간 범위
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        
        # mid 시간 동안 심사할 수 있는 사람 수 계산
        total = 0
        for time in times:
            total += mid // time
            if total >= n:  # 이미 n명 이상이면 더 계산할 필요 없음
                break
        
        if total >= n:
            answer = mid  # 더 적은 시간으로 시도
            right = mid - 1
        else:
            left = mid + 1  # 시간이 부족하므로 늘림
    
    return answer
