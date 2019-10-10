def solution(X, Y, D):
    if X <= Y:
        return int(-(-(Y-X)//D)) 