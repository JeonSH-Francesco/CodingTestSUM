def solution(name):
    answer = 0
    n = len(name)
    
    # 세로 조작: 각 문자를 목표 문자로 변경하는 최소 횟수 계산
    for char in name:
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
    
    # 기본적으로 오른쪽으로만 이동할 경우의 횟수
    move = n - 1
    
    # 좌우 조작 최적화: 연속된 'A'들을 건너뛰는 전략
    for i in range(n):
        next = i + 1
        while next < n and name[next] == 'A':
            next += 1
        # 두 가지 경우 중 최소 이동 횟수를 선택
        move = min(move, 2 * i + n - next, i + 2 * (n - next))
    '''
    세 가지 후보 이동 경로:
    경로 0 = move 기본적으로 오른쪽으로만 이동한 경우
    
    경로 1= 2 * i + n - next
    오른쪽으로 i번 이동하여 현재 인덱스에 도달한 후, 방향을 반대로 바꿔(왼쪽으로) 돌아가야 할 경우
    여기서 2 * i는 오른쪽 이동 후 돌아오는 비용이고, n - next는 연속된 'A'를 건너뛴 후 나머지 문자를 처리하기 위한 추가 이동 횟수
    
    ->언제 유리한가?
    만약 앞쪽(즉, 초기 인덱스까지 이동한 후)으로 빠르게 돌아가서 다시 오른쪽 끝에 가까운 문자를 처리하는 것이 효율적일 때 사용
    
    경로 2= i + 2 * (n - next)
    오른쪽으로 i번 이동한 후, 반대로 남은 부분을 두 번의 이동(앞뒤 왕복)으로 처리하는 경우
    여기서 i에 도달한 후, 남은 오른쪽 구간(연속된 'A' 이후)의 문자를 처리하기 위해 2*(n-next)는 인덱스 n - next 만큼 이동후 돌아오는 비용
    ->언제 유리한가?
    만약 연속된 'A' 구간 이후의 문자까지 한 번에 접근하는 것보다, 오른쪽으로 이동한 후 그 구간을 왕복해서 처리하는 것이 효율적일 때 사용
    '''
    answer += move
    return answer
print(solution('JEROEN'))
print(solution('JAN'))
