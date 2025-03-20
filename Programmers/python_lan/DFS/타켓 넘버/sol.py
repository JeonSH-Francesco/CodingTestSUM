def solution(numbers, target):
    #DFS함수 정의 : index 번째 숫자를 처리하면서, 현재가지의 합을 total로 유지
    def dfs(index, total):
        #모든 숫자를 다 사용했을 때 (index가 끝까지 도달한 경우)
        if index == len(numbers):
            #누적된 합이 target과 같으면 1을 반환하여 경우의 수를 증가
            if total==target:
                return 1
            else:
                return 0
        
        #현재 숫자를 더하는 경우와 빼는 경우를 각각 탐색
        count=0
        count += dfs(index+1,total+numbers[index]) #현재 숫자를 더하는 경우
        count += dfs(index+1,total-numbers[index]) #현재 숫자를 빼는 경우
        return count
    return dfs(0,0) #탐색 시작

test_case1=[1, 1, 1, 1, 1]
test_case2=[4, 1, 2, 1]


print(solution(test_case1,3))
print(solution(test_case2,4))

