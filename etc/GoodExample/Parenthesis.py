def solution(expression):
    #x기호를 *로 통일
    expression=expression.replace("x","*")

    tokens=[]
    num=""
    
    for ch in expression:
        if ch.isdigit():
            num+=ch
        else:
            #숫자는 숫자끼리 묶어서 append
            tokens.append(num)
            #연산자는 연산자 끼리 묶어서 append
            tokens.append(ch)
            num=""#다음 숫자 묶기 위한 num 초기화 과정 필수
    #마지막에는 연산자 이후가 없으므로 한번 더 수행           
    tokens.append(num)
    
    #최댓값을 물었으므로
    max_value=-float('inf')
    
    #숫자 위치 기준으로 괄호 시작/끝 선택
    #숫자는 짝수 인덱스에 존재
    for start in range(0,len(tokens),2):
        for end in range(start,len(tokens),2):
            #얕은 복사 수행하여 new_tokens 리스트 선언
            new_tokens=tokens[:]
            #숫자는 앞,뒤에 괄호를 삽입하여 new_tokens의 얕은 복사한 리스트에 삽입
            new_tokens.insert(start,"(")
            #start를 기준으로 2번째 뒤에 괄호를 묶어줘야 하므로
            new_tokens.insert(end+2,")")
            
            expr="".join(new_tokens)
            value=eval(expr)
            max_value=max(value,max_value)
    
    return max_value


expression = "2-1x5-4x3+2"
expression1 = "10+2x3-4"

print(solution(expression)) #11 ->"2-(1x5-4x3)+2"
print(solution(expression1)) #32 -> "(10+2)x3-4"
