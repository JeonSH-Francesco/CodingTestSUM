# A: 삭제를 고려하지 않은, 개미의 좌표(좌표를 -1로 바꾸는 것을 삭제로 구현)

'''
1. 추가:
    - 리스트의 마지막에 추가
2. 삭제
    - 리스트에서 해당 인덱스를 -1로 변경
3. 정찰 (r)
    parametric search로 구현
        결정 : 길이 t인 r개의 막대기로 모든 점을 덮을 수 있는가?
'''

Q= int(input()) #여왕 개미가 내린 명령의 수
#첫 번째 입력을 받는데, 맨 처음은 100으로 시작하므로 _로 표시하고 
#다음은 N으로 개미집 개수, *A로 나머지 숫자를 리스트로 받는다.
_ , N, *A = map(int,input().split()) 

def build(p):
    A.append(p)

def destroy(idx):
    A[idx]=-1

def can_patrol(B,r,t):
    x=B[0]
    cnt=1
    for b in B:
        if b>x+t:
            x=b
            cnt+=1
    return cnt<=r

def patrol(r):
    #a에 -1이 아닌 원소로만 구성하여 리스트를 구현
    real_A = [a for a in A if a!=-1]
    #left는 무조건 불가능한 값 , right : 무조건 가능한 값
    left, right = 0, 10**9

    while left<right:
        mid = (left+right)//2
        #정찰이 더 짧은 막대기로도 가능하니 left~mid사이로 범위를 설정
        if can_patrol(real_A,r,mid):
            right=mid
        #정찰이 mid로는 불가능하니 mid~right로 범위를 설정
        else:
            left=mid+1
    return left


for _ in range(Q-1):
    cmd, value = map(int,input().split())
    if cmd==200:
        build(value)
    elif cmd==300:
        destroy(value-1)
    elif cmd==400:
        print(patrol(value))
        
'''
입력



7
100 5 2 4 7 8 15
400 1
400 2
200 50
400 2
300 5
400 3


나의 출력
13
6
13
2

정답
13
6
13
2
'''
