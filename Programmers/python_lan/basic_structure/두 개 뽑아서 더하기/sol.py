def solution(numbers):
    temp = set()
    
    # 모든 두 수의 합 저장
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            temp.add(numbers[i] + numbers[j])

    return sorted(temp)  # 정렬 후 반환

# 테스트
numbers = [2, 1, 3, 4, 1]
result = solution(numbers)
print(result)
