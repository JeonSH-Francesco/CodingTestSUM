from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    q=deque()
    visited=set()
    
    q.append((begin,0)) # (현재 단어, 변환 횟수) 형태로 큐에 추가
    # 큐가 빌 때까지 반복 (BFS 탐색)
    while q:
        word,steps=q.popleft() #현재 단어와 변환 횟수 꺼냄
        #target이 같아진 경우 변환 횟수 반환
        if word==target:
            return steps
        #words배열을 순회하면서
        for next_word in words:
            #다음 단어를 돌지 않았으면 diff_count=0으로 초기화 한 후
            if next_word not in visited:
                diff_count=0
                #begin(word),next_word를 각각 비교했을 때
                for a,b in zip(word,next_word):
                    #글자가 다른 경우가 있으면 diff_count 증가
                    if a!=b:
                        diff_count+=1
                #정확히 한 글자만 다른 경우
                if diff_count==1:
                    #방문 처리
                    visited.add(next_word)
                    #next_word와 steps+1 큐에 추가
                    q.append((next_word,steps+1))
                    
    #변환이 불가능 한 경우
    return 0
