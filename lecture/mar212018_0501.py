def merge(L1, L2):
    L = []
    i1 = i2 = 0
    while i1 < len(L1) and i2 < len(L2):  # While both indecies not exceed.
        if L1[i1] < L2[i2]:
            L.append(L1[i1])
            i1 += 1
        else:
            L.append(L2[i2])
            i2 += 1
    return L + L1[i1:] + L2[i2:]


def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        return merge(
            merge_sort(L[:len(L) // 2]),  # Log n times
            merge_sort(L[len(L) // 2:])
            )
            
            