def solution(m,temperatures,clothes):
    n=len(temperatures)
    
    #각 온도별 최대 커버 범위 저장
    #특정 온도를 만났을 때, 어디까지 커버 가능한 옷이 있는가를 저장하기 위함.
    cover={}
    
    for low,high in clothes:
        for temp in range(low,high+1):
            #temp를 커버 가능한 옷 중 가장 높은 high 저장
            if temp not in cover:
                cover[temp]=high
            else:
                cover[temp]=max(cover[temp],high)
                
    best_start = 1
    best_count = float('inf')
    
    for start in range(n-m+1):
        #중복 제거 + 정렬
        temps=sorted(set(temperatures[start:start+m]))
        
        idx=0
        count=0
        
        while idx<len(temps):
            #아직 커버하지 않은 가장 작은 온도
            current = temps[idx]
            
            #current를 포함하는 옷들 중 가장 멀리(높은 온도까지)커버 가능한 끝점
            best_end = cover[current]
            #옷 하나 선택
            count+=1
            
            #방금 선택한 옷으로 커버 가능한 온도들은 전부 건너뜀
            while idx<len(temps) and temps[idx] <= best_end:
                idx+=1
                
        #현재 시작일의 옷 개수가 더 적다면 정답 갱신
        if count < best_count:
            best_count = count
            best_start = start+1#0-indexed->1-indexed
            
    return best_start
            


print(solution(3, [25, 30, 15, 20],[[13, 21], [18, 25], [26, 30]]))

print(solution(4,[-10, 20, 20, 20, -10, 20, 20, 20, 20, -10],[[-15, 15], [15, 25]]))

print(solution(4,[-2, -1, 0, 1, 2, 3, 4, 5, 6, 7],[[-100, 0], [0, 100]]))

print(solution(2,[-9, 13, 13, -8, 20, 6],[[-10, 0], [1, 13], [13, 25]]))
