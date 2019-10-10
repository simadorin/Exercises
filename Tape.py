def solution(A):
    a=A
    tablica=[]
    tablica1=[]
    suma=0
    if len(a) == 2:
        return abs(a[0]-a[1])
    for x in a:
        suma  += x
        tablica.append(suma)
    for i in range(len(tablica)-1):
        wynik=(suma-2*tablica[i])
        tablica1.append(abs(wynik))
    tablica1.sort()
    return tablica1[0]