def solution(asset,array):
    result = 0
    #print(asset)
    n,m,k = map(int,asset.split())
    data = list(map(int,array.split()))
    '''
    #이부분
    n,m,k = map(int,input().split())
    data = list(map(int,input().split()))
    #로도 가능
    '''

    data.sort()
    max = data[-1]
    mid=data[-2]
    
    '''
    #틀린 방법
    time = k*(m//k)
    result += max*time
    result += mid*(m-time)
    '''
   
    time = m//(k+1) #mid가 곱해지는 반복수
    result += mid*time
    result += max*(m-time)


    return result


state = input("처음 숫자: ")
arr = input("두번째 숫자 : ")
print(solution(state,arr))