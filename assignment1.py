import sorting_algorithms_steps.insertion_sort as sa
import sorting_algorithms_steps.merge_sort
import sorting_algorithms_steps.quick_sort
import sorting_algorithms_steps.heap_sort
import random
import matplotlib.pyplot as plt
import random
import time


number_of_elements = []
number_of_steps_insertion = []
number_of_steps_merge = []
number_of_steps_quick = []
number_of_steps_heap = []

for n in range(10, 1001, 20):
    arr = []
    for j in range(n):
        arr.append(random.randint(1, 10000))

    number_of_elements.append(len(arr))


    # insertion
    _, steps_insertion = sa.insertion_sort(arr)
    number_of_steps_insertion.append(steps_insertion)


    # merge
    steps_merge = sorting_algorithms_steps.merge_sort.merge_sort(arr, 0, len(arr) - 1)
    number_of_steps_merge.append(steps_merge)

    # quick
    steps_quick = sorting_algorithms_steps.quick_sort.quick_sort(arr, 0, len(arr) - 1)
    number_of_steps_quick.append(steps_quick)

    # heap
    steps_heap = sorting_algorithms_steps.heap_sort.heap_sort(arr)
    number_of_steps_heap.append(steps_heap)


plt.plot(number_of_elements, number_of_steps_insertion, label="Insertion sort (n²)")
plt.plot(number_of_elements, number_of_steps_quick, label="quick sort (n²)")
plt.plot(number_of_elements, number_of_steps_merge, label="merge sort (n log(n))")
plt.plot(number_of_elements, number_of_steps_heap, label="heap sort (n log(n))")
plt.xlabel("Input size (n)")
plt.ylabel("Steps")
plt.title("Sorting: Steps vs Input Size (Random inputs)")
plt.legend()
plt.show()





#------------------------------ Task 2


def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key

sizes = [1000, 5000, 10000, 20000]
for n in sizes:
    arr = [random.randint(1, 100000) for _ in range(n)]
    start = time.time()
    insertion_sort(arr)
    end = time.time()
    print(f"Python: Insertion Sort n={n}, time={end-start:.6f} seconds")