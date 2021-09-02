HH = int(input())

reNum=0

for hour in range(HH+1):
    if hour//10 == 3 or hour%10 ==3:
        reNum += 60*60
        continue

    for min in range(60):
        if min//10 ==3 or min%10 ==3:
            reNum += 60
            continue
        for sec in range(60):
            if (sec//10==3 or sec%10== 3):
                reNum +=1
                continue

print(reNum)            

reNum=0

#숫자를 문자열로 바꿔서 in을 사용할수 있음

for i in range(HH+1):
    for j in range(60):
        for k in range(60):
            if "3" in str(i)+str(j)+str(k):
                reNum +=1 

print(reNum)