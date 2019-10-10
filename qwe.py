def xo(s):
    os = []
    xs = []
    for i in s:

        if i == 'o':
            os.append(i)
        elif i == 'x':
            xs.append(i)
    if len(os) == len(xs):
        return True


print(xo('xo'))