def calculate_time(diffs,times,level):
    total_time=0 # 총 걸린 시간
    n=len(diffs) #문제 개수
    
    for i in range(n):
        #현재 레벨이 문제 난이도보다 높거나 같으면
        if diffs[i]<=level:
            total_time+=times[i] #틀리지 않고 문제 해결
        else:
            if i>0:
                prev_time=times[i-1]
            else:
                prev_time=0
            #diff>level이면 퍼즐을 총 diff-level번 틀리고    
            mistakes=diffs[i]-level
            total_time+=mistakes*(times[i]+prev_time)+times[i]
            #틀릴 때마다 time_cur만큼의 시간을 사용하며 
            #추가로 time_prev만큼의 시간을 사용해 이전 퍼즐을 다시 풀고 와야 함.
        
        # 매우 큰 경우 제한
        if total_time >10**18:
            return total_time

    return total_time
        
def solution(diffs, times, limit):
    answer = 0
    left, right=1,100000 # 레벨 탐색 범위
    
    while left<=right:
        mid=(left+right)//2  # 현재 레벨 가정
        # mid 레벨로 모든 문제를 limit 시간 내 해결 가능한지 확인
        if calculate_time(diffs,times,mid)<=limit:
            answer=mid
            right=mid-1
        else:
            left=mid+1
    return answer
    

'''
ref : 
https://school.programmers.co.kr/learn/courses/30/lessons/340212
'''
