def solution(n):
    s=str(n)
    L=len(s)
    answer=[]
    
    for i in range(L-1,-1,-1):
        answer.append(int(s[i]))
    return answer
