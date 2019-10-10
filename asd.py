def moves(a):
    b = 0
    count = 0
    for i in range(0, len(a)):

        if a[i] % 2 == 0:
            print(a[i])
            a[i] = a[b]
            a[b] = a[i]
            count = count + 1
            a[b] = a[b+1]
            a[i] = a[i+1]
        return count

print(moves([2,3,5,6,8]))