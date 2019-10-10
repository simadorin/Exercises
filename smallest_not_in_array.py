from itertools import count, filterfalse
def solution(A):
    return (next(filterfalse(set(A).__contains__, count(1))))