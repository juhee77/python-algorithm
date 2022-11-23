n,m= map(int,input().split(" "))
sixMin = 10000;
oneMin = 10000;
for i in range(m):
  six,one = map(int,input().split(" "))
  sixMin = min(sixMin,six)
  oneMin = min(oneMin,one)

sixCnt = n // 6
oneCnt = n % 6
print(min(min(oneMin*n,sixCnt*sixMin+oneCnt*oneMin),(sixCnt+1)*sixMin))