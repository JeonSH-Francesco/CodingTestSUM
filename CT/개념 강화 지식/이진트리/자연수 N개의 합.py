import math

S = int(input().strip())
print((math.isqrt(1 + 8*S) - 1) // 2)

'''
1~N까지의 자연수의 합이 S이하인 경우 중 가능한 N의 최댓값을 구하는 프로그램을 작성하세요
S = int(input().strip())

left, right = 0, 2*10**9

while left<right:
    mid = (left+right+1)//2
    if mid*(mid+1) //2 <=S:
        left= mid
    else:
        right=mid-1

print(left)
'''
