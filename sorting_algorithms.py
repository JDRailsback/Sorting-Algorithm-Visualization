import numpy as np

def insertion_sort(arr):
    for k in range(1, len(arr)):
        cur = arr[k]
        j = k
        while j > 0 and arr[j - 1] > cur:
            arr[j] = arr[j - 1]
            j -= 1
            yield arr, [j, j+1]
        arr[j] = cur
        yield arr, [j]
    yield arr, []
    return arr, []

def selection_sort(arr):
    for k in range(len(arr)):
        minloc = k
        for j in range(k + 1, len(arr)):
            if arr[j] < arr[minloc]:
                minloc = j
            yield arr, [j, minloc]
        arr[k], arr[minloc] = arr[minloc], arr[k]
        yield arr, [k, minloc]
    yield arr, []
    return arr, []

def bubble_sort(arr):
    for k in range(len(arr)):
        swap = False
        for j in range(len(arr) - k - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
            yield arr, [j, j+1]
        if not swap:
            break
    yield arr, []
    return arr, []

def merge_sort(arr, start=0):
    if len(arr) <= 1:
        yield arr, []
        return
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    for state, idx in merge_sort(left, start=start):
        arr[:mid] = state
        yield arr, idx
    for state, idx in merge_sort(right, start=start+mid):
        arr[mid:] = state
        yield arr, idx

    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        yield arr, [start+k]
        k += 1
    while i < len(left):
        arr[k] = left[i]
        yield arr, [start+k]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        yield arr, [start+k]
        j += 1
        k += 1
    yield arr, []

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        yield arr, [i, 0]
        yield from heapify(arr, i, 0)
    yield arr, []

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        yield arr, [i, largest]
        yield from heapify(arr, n, largest)

def bogo_sort(arr):
    while not is_sorted(arr):
        shuffle(arr)
        yield arr, list(range(len(arr)))
    yield arr, []
    return arr, []

def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def shuffle(arr):
    n = len(arr)
    for i in range(n):
        r = np.random.randint(0, n)
        arr[i], arr[r] = arr[r], arr[i]

sorters = {
    "Insertion": insertion_sort,
    "Selection": selection_sort,
    "Bubble": bubble_sort,
    "Merge": merge_sort,
    "Heap": heap_sort,
    "Bogo": bogo_sort,
    "insertion": insertion_sort,
    "selection": selection_sort,
    "bubble": bubble_sort,
    "merge": merge_sort,
    "heap": heap_sort,
    "bogo": bogo_sort,
}