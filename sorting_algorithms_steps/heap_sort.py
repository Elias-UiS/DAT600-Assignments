
def heapify(arr, n, i):
    step = 0
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n:
        step += 1
        if arr[l] > arr[largest]:
            largest = l

    if r < n:
        step += 1
        if arr[r] > arr[largest]:
            largest = r
    

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        step += 1
        step += heapify(arr, n, largest)

    return step

def heap_sort(arr):
    step = 0
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        step += heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        step += 1
        step += heapify(arr, i, 0)
    return step
