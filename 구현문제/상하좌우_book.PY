n = int(input())
instr = input().split()

x,y= 1,1
nx,ny=1,1
dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_types=["L","R","U","D"]

for plan in instr:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y+ dy[i]
    if nx<1 or ny<1 or n<nx or n<ny:
        continue
    x,y=nx,ny
print("%d  %d"%(x,y))