import heapq

def solution(scoville, K):
    #섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 +(두 번째로 맵지 않은 음식의 스코빌 지수*2)
    #최소 힙으로 변환
    heapq.heapify(scoville)
    mix_count=0 #섞은 횟수
    
    #스코빌 지수가 K 이상이 될 때까지 반복 하여 섞는다.
    #가장 낮은 스코빌 지수가 K 미만일 때 계속 섞기
    while scoville[0]<K and len(scoville)>1:
        #가장 맵지 않은 두 음식 꺼내기
        first=heapq.heappop(scoville)
        second=heapq.heappop(scoville)
        
        #새 음식의 스코빌 지수 계산
        new_food = first+(second*2)
        heapq.heappush(scoville,new_food)
        
        mix_count+=1
    #반복문이 끝난 경우 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1
    if scoville[0]<K:
        return -1
    
    
    return mix_count
