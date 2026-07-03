def solution(teamIDs,additional):
    result= []
    existing = set(teamIDs) #이미 참가 중인 팀
    added=set() #추가모집 결과에 이미 넣은 팀
    
    for team in additional:
        #기존 팀에도 없고, result에도 아직 없는 경우만 추가
        if team not in existing and team not in added:
            result.append(team)
            #이미 result에 넣은 team을 기록하기 위해 added set에다가도 추가
            added.add(team)
            
    return result
    

teamIDs = ["world", "prog"]
additional = ["hello", "world", "code", "hello", "try", "code"]

teamIDs1 = ["red", "blue", "green"]
additional1 = ["yellow", "blue", "black", "yellow", "white", "green", "black"]

print(solution(teamIDs, additional)) # ['hello', 'code', 'try']
print(solution(teamIDs1, additional1)) # ['yellow', 'black', 'white']
