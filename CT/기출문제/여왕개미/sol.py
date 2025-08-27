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

Q = int(input())
_, N, *A = map(int,input().split())

def build(p):
    A.append(p)
    
def destroy(idx):
    A[idx]=-1

#B: 좌표 배열, r: 막대 개수, t: 막대 길이
def can_patrol(B,r,t):
    x=B[0]
    cnt=1
    for b in B:
        if b>x+t:
            x=b 
            cnt+=1
    return cnt <= r
    
def patrol(r):
    #a에 -1이 아닌 원소만 구성하여 리스트 구현
    real_A = [a for a in A if a!=-1]
    
    #left는 무조건 불가능한 값 , right : 무조건 가능한 값
    left,right = 0, 10**9
    
    while left<right:
        mid=(left+right)//2
        if can_patrol(real_A,r,id):
            right=mid
        else:
            left=mid+1
            
    return left
    


for _ in range(Q-1):
    cmd, value = map(int,input().split())
    if cmd ==200:
        build(value)
    elif cmd ==300:
        destroy(value-1)
    elif cmd ==400:
        print(patrol(value))
