n = int(input())
inputArr =  list(map(int,input().split()))
arr = [[0 for i in range(n+1)] for j in range(n+1)] 
sum = [0 for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,i+1):
        if(inputArr[j-1]<inputArr[i-1]):
            arr[i][j] =max(arr[i][j-1],arr[j][j])
        elif(i==j) :
            arr[i][j] =arr[j][j-1]+1
        else:
            arr[i][j] = arr[i][j-1]
    sum[i] = arr[i][i]

maxSum = max(sum)
idx = n
sb = ""
while 0<idx:
    if maxSum == sum[idx]:
        sb = str(inputArr[idx-1])+ " "+ sb
        maxSum -= 1
    idx -= 1

print(str(max(sum))+"\n"+sb)
    