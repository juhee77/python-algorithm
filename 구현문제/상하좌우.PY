inNum = int(input())
inStr = list(input().split())


R,L,U,D=0,0,0,0
for c in inStr:
    if c == "L":
        if 1 <= R+L and R+L <=5:
            L+=1
    elif c == "R":
        if 0 <= R+L and R+L <=5:
            R+=1
    elif c == "U":
        if 1 <= U+D and U+D <=5:
            U += 1
    elif c == "D":
        if 0 <= U+D and U+D <=5:
            D += 1
print(str(D-U+1)+" "+str(R-L+1))
        