def solution(s):
    answer = True
    balance=0
    n=len(s)
    
    for i in range(n):
        if s[i]=='(':
            balance+=1
        else:
            balance-=1
        if balance<0:
            answer=False
            break
    if balance!=0:
        answer=False
        
    return answer

    return True
