def calculate_time(diffs,times,level):
    total_time=0 #전체 걸린 시간
    n=len(diffs) #전체 턴수 계산
    
    for i in range(n):
        if diffs[i]<=level: #레벨이 모든 난이도보다 큰 경우 전부 손쉽게 풀 수 있으므로
            total_time+=times[i] #틀리지 않고 걸리는 시간을 더해주면 된다.
        else: #그렇지 않은 경우
            if i >0: 
                prev_time=times[i-1] #이전 시간 계산하기
            else:
                prev_time=0
                
        mistakes=diffs[i]-level #문제 조건에 따라 난이도와 현재 레벨의 차이만큼 틀리므로 mistakes 정의하고
        total_time=mistakes*(times[i]+prev_time)+times[i] #total_time을 계산
        
        if total_time>10**18: #만약 total_time이 엄청 큰 경우는 그냥 return
            return total_time # 충분히 큰 수로 제한 (안전장치)
    
    return total_time #return 총 걸린 시간
    
def solution(diffs, times, limit):
    left, right=1, 1000000
    answer=right
    #left, right, answer를 초기화 해준다
    
    #이분 탐색->최솟값이 되는 경우가 될 때가지
    while left<=right:
        mid=(left+right)//2
        #제한된 시간 안에 풀 수 있는 경우->최솟값을 구하기 위해 right를 줄여서 계산한다.
        if calculate_time(diffs,times,mid)<=limit:
            answer=mid
            right=mid-1
        #제한된 시간 안에 풀지 못하는 경우->최솟값을 구하기 위해 left를 늘려서 계산한다.
        else:
            left=mid+1
    return answer
'''
ref : 
https://school.programmers.co.kr/learn/courses/30/lessons/340212
'''
