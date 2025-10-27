def calculate_time(diffs, times, level):
    total_time = 0  # 누적 총 걸린 시간
    n = len(diffs)   # 문제 개수
    
    for i in range(n):
        # 현재 레벨이 문제 난이도보다 높거나 같으면
        if diffs[i] <= level:
            total_time += times[i]  # 틀리지 않고 문제 해결
        else:
            # 난이도 > 레벨이면 틀림 발생
            mistakes = diffs[i] - level  # 틀리는 횟수
            
            # 이전 문제 시간을 가져와야 하는데 첫 문제면 0
            if i > 0:
                prev_time = times[i-1]
            else:
                prev_time = 0
            
            # 틀린 횟수만큼 시간 누적 + 현재 문제 시간 추가
            total_time += mistakes * (times[i] + prev_time) + times[i]
        
        # 매우 큰 경우 제한
        if total_time > 10**18:
            return total_time
    
    return total_time

def solution(diffs, times, limit):
    answer = 0
    left, right = 1, 100000  # 레벨 탐색 범위
    
    # 이분 탐색
    while left <= right:
        mid = (left + right) // 2  # 현재 레벨 가정
        # mid 레벨로 모든 문제를 limit 시간 내 해결 가능한지 확인
        if calculate_time(diffs, times, mid) <= limit:
            answer = mid        # 가능하면 answer 갱신
            right = mid - 1     # 더 낮은 레벨도 가능한지 확인
        else:
            left = mid + 1      # 불가능하면 레벨 올리기
    
    return answer


'''
ref : 
https://school.programmers.co.kr/learn/courses/30/lessons/340212
'''
