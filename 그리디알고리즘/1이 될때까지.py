m,n=map(int,input().split())

count = 0
while True:
    if m%n ==0 and 1<m:
        count += 1
        m /= n
    elif m%n !=0 and 1<m:
        m -=1 
        count +=1
    elif m<n:
        count += m-1
        break
    
print(int(count)) 