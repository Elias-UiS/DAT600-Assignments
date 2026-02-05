def partition(arr, low, high):
    step = 0

    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        step += 1
        if arr[j] < pivot:
            step += swap(arr, i + 1, high)
    
    step += swap(arr, i + 1, high)
    return i + 1, step

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return 1

def quick_sort(arr, low, high):
    step = 0
    if low < high:
        
        pi, steps = partition(arr, low, high)
        step += steps

        step += quick_sort(arr, low, pi - 1)
        step += quick_sort(arr, pi + 1, high)
    return step

