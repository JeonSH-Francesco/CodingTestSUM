def solution(operations):
    
    queue=[]
    
    for op in operations:
        #큐에 주어진 숫자 삽입
        if op[0]=="I":
            #int 처리!
            num=int(op[2:])
            queue.append(num)
        #최댓값 삭제
        elif op=="D 1":
            if queue:
                queue.remove(max(queue))
        #최솟값 삭제
        elif op=="D -1":
            if queue:
                queue.remove(min(queue))
    #큐가 비어있는 경우
    if not queue:
        return [0,0]
    #그렇지 않은 경우
    else:
        return [max(queue),min(queue)]
