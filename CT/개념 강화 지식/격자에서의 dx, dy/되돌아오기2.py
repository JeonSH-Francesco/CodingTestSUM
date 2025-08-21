commands = input()
n = len(commands)
x,y=0,0
dir=0 # 0 : 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
dxy=[(-1,0),(0,1),(1,0),(0,-1)]

time=0

for i in range(n):
    cmd = commands[i]
    time+=1
    if cmd=='L':
        dir = (dir-1)%4
    elif cmd=='R':
        dir = (dir+1)%4
    elif cmd=='F':
        dx, dy = dxy[dir]
        x+=dx
        y+=dy

    if x==0 and y==0:
        print(time)
        break

else:
    print(-1)
