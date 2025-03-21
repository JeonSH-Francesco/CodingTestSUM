def solution(elements):
    n=len(elements)
    elements = elements*2 #원형 수열을 구현하기 위해 2배 확장
    sums=set()
    
    for size in range(1,n+1):#부분 수열의 길이
        for i in range(n): #부분 수열의 시작 인덱스
            sums.add(sum(elements[i:i+size]))
            
    return len(sums)

elements1=[7,9,1,1,4]

print(solution(elements1))
