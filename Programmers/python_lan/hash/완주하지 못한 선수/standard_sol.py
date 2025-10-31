from collections import Counter

def solution(participant, completion):
    participant_count = Counter(participant)
    completion_count = Counter(completion)
    
    for name in participant_count:
        if participant_count[name] != completion_count.get(name, 0):
            return name
