n = int(input())
inputArr =  list(map(int,input().split()))
sum = [1 for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,i+1):
        if(inputArr[j-1]<inputArr[i-1]):
            sum[i] =max(sum[i]+1,sum[j])

maxSum = max(sum)
idx = n
sb = ""
while 0<idx:
    if maxSum == sum[idx]:
        sb = str(inputArr[idx-1])+ " "+ sb
        maxSum -= 1
    idx -= 1

print(str(max(sum))+"\n"+sb)
    