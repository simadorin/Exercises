from collections import Counter

def sockMerchant(n, ar):
    res = [k for k, v in Counter(ar).items() for _i in range(v // 2)]