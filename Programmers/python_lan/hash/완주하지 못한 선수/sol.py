def solution(participant, completion):
    #두 리스트를 정렬
    participant.sort()
    completion.sort()
    
    #정렬된 두 리스트르 비교하여 다르면 그 선수가 완주하지 못한 선수
    for i in range(len(completion)):
        if participant[i] !=completion[i]:
            return participant[i]
        
    #모든 선수가 일치하면 마지막 선수가 완주하지 못한 선수
    return participant[-1]
    
participant=["marina", "josipa", "nikola", "vinko", "filipa"] 
completion=["josipa", "filipa", "marina", "nikola"]

print(solution(participant,completion))
