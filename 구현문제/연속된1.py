
Allcnt =0 
for i in range(100):
    cnt =0 
    num=i
    flag = 0
    while(num>1):
        if num%2==1:
            if(flag==1):
                cnt +=1 
                if(cnt ==2):
                    Allcnt +=1
                    print(i,end="  ")
                    break
            else:
                flag =1
        else:
            flag = 0
        num //= 2
    
    if num ==1 and flag==1:
        Allcnt +=1
        print(i,end="  ")


print("\n%d"%Allcnt)
    