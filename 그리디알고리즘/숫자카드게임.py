
n,m=map(int,input().split())
minData=-10000
for i in range(n):
    inputList=list(map(int,input().split()))
    
    if minData <= min(inputList):
        minData=min(inputList)

    #위에 두줄 생략하고 그냥
    #minData=max(minData,min(inputList))

print(minData)
