"""
This is a pure Python implementation of the heap sort algorithm.

"""


def heapify(arr, heap_size, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < heap_size and arr[largest] < arr[left]:
        largest = left
    if right < heap_size and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, heap_size, largest)


def heap_sort(arr):
    a = len(arr)

    for i in range(int(a/2 - 1), -1, -1):
        heapify(arr, a, i)
    for i in range(a-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


if __name__ == "__main__":
    unsort_array = [1, 4, 7, 2, 1, 3, 2, 5, 4, 2]
    unsort_array2 = [8, 7, 6, 5, 4, 3, 2, 1]
    print(heap_sort(unsort_array))
    print(heap_sort(unsort_array2))
