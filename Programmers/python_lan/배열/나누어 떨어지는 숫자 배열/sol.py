def solution(arr, divisor):
    n=len(arr)
    answer=[]
    
    for i in range(n):
        if arr[i]%divisor==0:
            answer.append(arr[i])
    if len(answer)==0:
        answer.append(-1)
    
    answer.sort()
            
    return answer
