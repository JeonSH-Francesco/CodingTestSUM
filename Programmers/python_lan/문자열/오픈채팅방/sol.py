def solution(record):
    user_dict = {}
    log = []
    
    for entry in record:
        parts = entry.split()
        if parts[0] == "Enter":
            user_dict[parts[1]] = parts[2]
            log.append((parts[1], "님이 들어왔습니다."))
        elif parts[0] == "Leave":
            log.append((parts[1], "님이 나갔습니다."))
        elif parts[0] == "Change":
            user_dict[parts[1]] = parts[2]
            
    return [user_dict[user_id] + action for user_id, action in log]

# 테스트 케이스
test_cases = [
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"],
    ["Enter uid1000 Alice", "Enter uid2000 Bob", "Leave uid1000", "Change uid2000 Charlie", "Enter uid1000 Dave"],
    ["Enter uid9999 Eve", "Leave uid9999", "Enter uid9999 Eve", "Change uid9999 Adam"],
]

# 결과 출력
for i, test_case in enumerate(test_cases):
    print(f"Test Case {i+1}: {solution(test_case)}")
