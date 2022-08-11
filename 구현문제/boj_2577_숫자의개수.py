max = 1

for i in range(3):
    max *= int(input())

s = str(max)
for i in range(10):
    print(s.count(str(i)))
