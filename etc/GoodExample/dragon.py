def solution(n):
    if n == 0:
        return 1
    
    dragons = [0] * (n + 1)
    dragon_eggs = [0] * (n + 1)
    
    dragon_eggs[0] = 1
    
    for day in range(1, n + 1):
        # 현재 날짜에서 알을 낳을 수 있는 드래곤 수 계산
        dragon_eggs[day] = dragons[day - 1] if day - 1 >= 0 else 0
        
        # 현재 날짜에서 부화한 드래곤 수 계산
        dragons[day] = dragons[day - 1] + dragon_eggs[day - 1] if day - 1 >= 0 else 1
        
        # 다섯 번 알을 낳은 후에 더 이상 알을 낳지 않도록 설정
        if day >= 5:
            dragon_eggs[day] -= dragon_eggs[day - 5]
    
    return dragons[n] + dragon_eggs[n]

# 예시 입력과 출력 테스트
for i in range(1,11):
    print(solution(i)) 
    
'''

1
2
3
5
7
12
18
29
45
72

'''
