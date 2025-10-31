from collections import deque

def solution(priorities, location):
    queue=deque([(p,i) for i,p in enumerate(priorities)])
    execution_order=0
    
    while queue:
        process=queue.popleft()
        if any(process[0]<P[0] for P in queue):
            queue.append(process)
        else:
            execution_order+=1
            if process[1]==location:
                return execution_order
    
