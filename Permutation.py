def solution(A):
    sum1 = 0
    for i in range(0,len(A)+1):
        sum1 = sum1+i
    if sum1 == sum(A):
        return 1
    else:
        return 0