from math import ceil

def solution(progresses, speeds):
    answer = []
    
    # 각 작업별로 완료까지 필요한 일수 계산
    days = [ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    # 현재 배포 기준이 되는 작업 완료 일수
    current = days[0]
    count = 1
    
    for i in range(1, len(days)):
        if days[i] <= current:
            # 현재 배포 기준일 이내에 끝나면 같이 배포
            count += 1
        else:
            # 더 늦게 끝나는 작업 나오면 이전 묶음 배포하고 새 기준 설정
            answer.append(count)
            current = days[i]
            count = 1
    # 마지막 묶음 배포
    answer.append(count)
    
    return answer
