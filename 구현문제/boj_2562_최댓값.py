
# max = 0
# index = -1
# for i in range(9):
#     temp = int(input())
#     if temp > max:
#         max = temp
#         index = i

# print(max)
# print(index+1)


# l=[int(input()) for i in range(9)]
# m=max(l)
# print(m)
# print(l.index(m)+1)

#숫자의 합 11720
#sol1
# line = int(input())
# a = input()
# sum =0
# for i in range (line) :
#     sum += int(a[i])
# print(sum)

#sol2
# input();print(sum(map(int,input())))

#sol3
# input()
# print(sum(map(int, input())))


# while True:
#     try:
#         A, B= map(int,input().split())
#         print(A+B)
#     except: #파일끝 처리방법
#         break


# for i in range (int(input())):
#     A, B= map(int,input().split())
#     print(A+B)
    
# input()
# arr =list(map(int,input().split()))
# print(min(arr),max(arr))

# line = int(input())
# for i in range (line):
#     arr = input()
#     sum = 0
#     temp=1
#     for j in arr:
#         if j=="O":
#             sum+= temp
#             temp += 1
#         else :
#             temp=1
#     print(sum)

# s = input()
# if s== "1 2 3 4 5 6 7 8" : print("ascending")
# elif s=="8 7 6 5 4 3 2 1": print("descending")
# else: print("mixed")

# s= int(input())
# if 90<= s <=100: print("A")
# elif 80<= s <=89: print("B")
# elif 70<= s <=79: print("C")
# elif 60<= s <=69: print("D")
# else: print("F")

#대문자 65_90 소문자 97-122
# s = input()
# for i in range (97,123):
#     print(s.find(chr(i)),end=" ")

# n = int(input())
# arr=list(range(1,n+1))

# while len(arr)>1:
#     arr = arr[1::2]

# print(arr[0])


# x= int(input())
# y = int(input())
# if 0<x:
#     if y<0: print(4)
#     else: print(1)
# else :
#     if y<0: print(3)
#     else: print(2)


x,y,z = map(int,input().split())
if x==y==z:
    print(10000+x*1000)
elif x==y:
    print(1000+x*100)
elif x==z:
    print(1000+x*100)
elif z==y:
    print(1000+y*100)
else :
    print(max(x,max(y,x)*100))