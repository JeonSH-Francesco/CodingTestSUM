import heapq

#작업의 번호, 작업의 요청 시각, 작업의 소요 시간을 저장해 두는 대기 큐

#우선순위
#작업의 소요 시간이 짧은 것, 작업의 요청 시각이 빠른 것, 작업의 번호가 작은 것 순

def solution(jobs):
    # 1. 작업들을 요청 시각 기준 정렬
    jobs.sort(key=lambda x: x[0]) 
    heap=[] #대기중인 작업을 저장할 힙
    
    #time은 현재 시각, 
    #i는 인덱스, 
    #total: 모든 작업의 반환 시간(종료시각 - 요청시각) 합계
    time,i,total=0,0,0 

    n=len(jobs) #작업의 길이
    
    # 2. 모든 작업을 처리할 때까지 반복
    while i<n or heap:
        # 3. 현재 시각(time)까지 도착한 모든 작업을 힙에 추가
        while i<n and jobs[i][0]<=time:
            #힙에는 (소요시간, 요청시각)형태로 저장->소요시간이 짧은 순으로 우선순위 결정
            heapq.heappush(heap,(jobs[i][1],jobs[i][0]))
            #(jobs[i][1],jobs[i][0])=(소요시간, 요청시간) heap에 추가
            i+=1
            
        # 4. 대기 중인 작업이 있다면 가장 짧은 작업을 꺼내 처리
        if heap:
            job=heapq.heappop(heap)
            time+=job[0] #현재 시각 += 작업 소요시간
            total+=time-job[1] #반환 시간 = 종료시각-요청시각
        else:
            # 5. 처리할 작업이 없다면 -> 다음 작업 요청 시각으로 이동
            time=jobs[i][0]
        
    # 6. 평균 반환 시간의 정수 부분반환
    return total//n
            
            
            
            
            
            
            
            
            
