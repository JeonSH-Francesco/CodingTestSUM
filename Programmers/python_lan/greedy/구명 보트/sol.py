def solution(people, limit):
    people.sort() #몸무게 오름차순 정렬
    left, right = 0, len(people)-1
    boats=0
    
    while left<=right:
        #가장 가벼운 사람과 무거운 사람을 함께 태울 수 있으면 함께 탐
        if people[left]+people[right]<=limit:
            left+=1 #가벼운 사람도 태웠으므로 이동
        #무거운 사람은 무조건 보트 필요
        right-=1
        boats+=1 #보트 개수 증가

    return boats


print(solution([70, 50, 80, 50], 100)) 
print(solution([70, 80, 50], 100)) 
