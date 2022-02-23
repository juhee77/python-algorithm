
# python_input.py
instr = list(input())
sum = 0
ans = []
'''
이부분을 그냥 
data = input()
for i in data 해서 하나씩 읽어오는 방법도 있음
'''

for i in range(0,len(instr)):
    if instr[i].isdigit():
        sum += int(instr[i])     
    else:
        ans.append(instr[i])
ans.sort()
ans = "".join(ans)
print(ans+str(sum))