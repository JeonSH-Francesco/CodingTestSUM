import heapq

def solution(jobs):
    jobs.sort(key=lambda x: x[0])  # 요청 시점 기준 정렬
    print(f"정렬된 작업 리스트: {jobs}")
    heap = []
    time, i, total = 0, 0, 0
    n = len(jobs)

    while i < n or heap:
        # 처리할 수 있는 작업들을 힙에 넣기
        while i < n and jobs[i][0] <= time:
            heapq.heappush(heap, (jobs[i][1], jobs[i][0]))
            print(f"시간 {time}: 작업 추가 - 실행시간 {jobs[i][1]}, 요청시점 {jobs[i][0]} / 힙 상태: {heap}")
            i += 1

        if heap:
            job = heapq.heappop(heap)
            print(f"시간 {time}: 작업 시작 - 실행시간 {job[0]}, 요청시점 {job[1]}")
            time += job[0]
            total += time - job[1]  # 작업 완료까지 걸린 시간(대기시간 포함)
            print(f"시간 {time}: 작업 완료 / 누적 총 대기시간: {total}")
        else:
            time = jobs[i][0]  # 처리할 작업이 없으면 다음 작업 요청 시간으로 이동
            print(f"시간 {time}: 대기 중 (다음 작업 요청 시점으로 이동)")

    print(f"총 작업 수: {n}, 평균 대기시간: {total // n}")
    return total // n

# 테스트 케이스 실행
jobs = [[0, 3], [1, 9], [3, 5]]
result = solution(jobs)
print(f"최종 반환값: {result}")

'''
ref: https://school.programmers.co.kr/learn/courses/30/lessons/42627

정렬된 작업 리스트: [[0, 3], [1, 9], [3, 5]]
시간 0: 작업 추가 - 실행시간 3, 요청시점 0 / 힙 상태: [(3, 0)]        
시간 0: 작업 시작 - 실행시간 3, 요청시점 0
시간 3: 작업 완료 / 누적 총 대기시간: 3
시간 3: 작업 추가 - 실행시간 9, 요청시점 1 / 힙 상태: [(9, 1)]        
시간 3: 작업 추가 - 실행시간 5, 요청시점 3 / 힙 상태: [(5, 3), (9, 1)]
시간 3: 작업 시작 - 실행시간 5, 요청시점 3
시간 8: 작업 완료 / 누적 총 대기시간: 8
시간 8: 작업 시작 - 실행시간 9, 요청시점 1
시간 17: 작업 완료 / 누적 총 대기시간: 24
총 작업 수: 3, 평균 대기시간: 8
최종 반환값: 8
'''
