import math


def mergesort(items, p, r):
    if p < r:
        q = math.floor((p+r)/2)   # int q
        mergesort(items, p, q)
        mergesort(items, q+1, r)
        merge(items, p, q, r)
    return items


def merge(items, p, q, r):
    n1 = q - p + 1  # 陣列大小
    n2 = r - q

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = items[p + i]

    for j in range(0, n2):
        R[j] = items[q + 1 + j]

    i = 0  # restart
    j = 0
    k = p

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            items[k] = L[i]
            i += 1
        else:
            items[k] = R[j]
            j += 1
        k += 1
    # 剩下沒排序到
    while i < n1:
        items[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        items[k] = R[j]
        j += 1
        k += 1


items = [2, 4, 5, 7, 1, 2, 3, 6]
items2 = [8, 7, 6, 5, 4, 3, 2, 1]
mergesort(items, 0, len(items)-1)
mergesort(items2, 0, len(items2)-1)
print(items)
print(items2)
