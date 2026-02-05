def insertion_sort(arr):
    step = 0
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0:
            step += 1             
            if arr[i] > key:
                arr[i + 1] = arr[i]
                step += 1         
                i -= 1
            else:
                break
        arr[i + 1] = key
        step += 1                 
    return arr, step