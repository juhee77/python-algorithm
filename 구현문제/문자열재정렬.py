
# python_input.py
instr = list(input())
sum = 0
ans = []
for i in range(0,len(instr)):
    if instr[i].isdigit():
        sum += int(instr[i])     
    else:
        ans.append(instr[i])
ans.sort()
ans = "".join(ans)
print(ans+str(sum))