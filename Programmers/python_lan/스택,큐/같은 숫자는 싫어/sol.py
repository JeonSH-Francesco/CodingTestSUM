def solution(arr):
    answer=[]
    prev=None
    
    for i in arr:
        if i!=prev:
            answer.append(i)
            prev=i
    return answer
