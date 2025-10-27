def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        temp = array[i-1:j]   # i번째부터 j번째까지 자름
        temp.sort()
        answer.append(temp[k-1])  # k번째 숫자 추가
    return answer
