def merge(list, l, m, r):
    step = 0
    n1 = m - l + 1
    step += 1
    n2 = r - m
    step += 1
    L = [0] * n1
    step += 1
    R = [0] * n2
    step += 1

    for i in range(n1):
        step += 1
        L[i] = list[l + i]
        step += 1
    for j in range(n2):
        step += 1
        R[j] = list[m + 1 + j]
        step += 1

    i = j = 0
    step += 1
    k = l
    step += 1

    while i < n1 and j < n2:
        step += 1
        if L[i] <= R[j]:
            step += 1
            list[k] = L[i]
            step += 1
            i += 1
            step += 1
        else:
            list[k] = R[j]
            step += 1
            j += 1
            step += 1
        step += 1
        k += 1
        step += 1

    while i < n1:
        step += 1
        list[k] = L[i]
        step += 1
        i += 1
        step += 1
        k += 1
        step += 1
    while j < n2:
        step += 1
        list[k] = R[j]
        step += 1
        j += 1
        step += 1
        k += 1
        step += 1

    return step

def merge_sort(list, l, r):
    step = 0
    if l < r:
        step += 1
        m = l + (r - l) // 2
        step += 1
        step += merge_sort(list, l, m)
        step += merge_sort(list, m + 1, r)
        step += merge(list, l, m, r)
    step += 1
    
    return step