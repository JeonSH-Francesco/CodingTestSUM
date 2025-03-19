def solution(v):
    #x_vals와 y_vals 리스트를 생성하여 x좌표와 y좌표를 각각 분리
    x_vals=[x for x, y in v] #v의 각 요소에서 x값만 추출하여 리스트 생성
    y_vals=[y for x,y in v] #v의 각 요소에서 y값만 추출하여 리스트 생성
    
    #리스트에서 한 번만 등장하는 x값을 찾음(직사각형의 네번째 꼭짓점 x좌표)
    x_missing =[x for x in x_vals if x_vals.count(x)==1][0]
    #리스트에서 한 번만 등장하는 y값을 찾음(직사각형의 네번쨰 꼭짓점 y좌표)
    y_missing =[y for y in y_vals if y_vals.count(y)==1][0]
    
    return [x_missing,y_missing]

v=[[1,4],[3,4],[3,10]]
print(solution(v))
    
#->[1,10]
