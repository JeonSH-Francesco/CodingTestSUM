def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance) #도착 지점도 바위처럼 처리하여 계산
    
    left=1
    right=distance
    answer=0
    
    while left<=right:
        mid=(left+right)//2
        prev=0
        remove_cnt=0
        
        for rock in rocks:
            if rock-prev<mid:
                remove_cnt+=1 #거리가 mid보다 짧으면 바위 제거
            else:
                prev=rock #유지한 바위 기준 갱신

        if remove_cnt>n:
            #너무 많이 제거된 경우-> 거리 줄여서 계산
            right=mid-1 
        else:
            #제거 수가 충분히 작거나 같은 경우-> 거리 늘려서 계산
            answer=mid
            left=mid+1

    
    return answer
