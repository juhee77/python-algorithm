tc = int(input())

for i in range(tc):
    n,m = input().split()
    for j in m :
        print(j * int(n),end="")
    print()





# H,M = map(int, input().split())
# if 0 <= H <= 23 and M - 45 >= 0: print(H, M - 45)
# elif 0 < H <= 23 and M - 45 < 0: print(H - 1, M + 15)
# elif H == 0 and M - 45 < 0: print(H + 23, M + 15)

#아스키코드
#print(ord(input()))

# n = int(input())
# if n%4==0 and (n%100 !=0 or n%400==0):
#     print("1")
# else:
#     print("0")



# n = int(input())

# for i in range(n,0,-1):
#     print(i)

# n=int(input())
# print("\n".join(map(str, range(n, 0, -1))))
