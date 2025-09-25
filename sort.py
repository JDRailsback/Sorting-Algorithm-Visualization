import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import copy
import time

# ---------------- Sorting Algorithms ----------------

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

# ---------------- Extra Functions ----------------

def gen_arr(size):
    return [np.random.randint(0, 10000) for _ in range(size)]

def update_bars(frame, bar_rects, base_color, highlight_color):
    arr, active = frame
    if not active and is_sorted(arr):
        for i, rect in enumerate(bar_rects):
            rect.set_height(arr[i])
            rect.set_color("green")
    else:
        for i, rect in enumerate(bar_rects):
            rect.set_height(arr[i])
            if i in active:
                rect.set_color(highlight_color)
            else:
                rect.set_color(base_color)
    return bar_rects

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

def run_sort_timing(sorter_func, arr):
    arr_copy = copy.deepcopy(arr)
    start = time.perf_counter()
    for _ in sorter_func(arr_copy):
        pass
    return time.perf_counter() - start


# ---------------- Main Program ----------------
if __name__ == '__main__':
    sorter_1 = input('Enter your first contender: ')
    while sorter_1 not in sorters:
        if sorter_1.lower() == 'help':
            print('Available sorting algorithms:')
            print(", ".join(list(sorters.keys())[:6]))
        else:
            print("Not a valid sorting algorithm. Type 'help' for a list of valid algorithms.")
        sorter_1 = input('Enter your first contender: ')

    sorter_2 = input('Enter your second contender: ')
    while sorter_2 not in sorters:
        if sorter_2.lower() == 'help':
            print('Available sorting algorithms:')
            print(", ".join(list(sorters.keys())[:6]))
        else:
            print("Not a valid sorting algorithm. Type 'help' for a list of valid algorithms.")
        sorter_2 = input('Enter your second contender: ')

    size = int(input('Enter size of lists to be sorted (<=1000): '))
    while size > 1000:
        print('Please choose a size of 1000 items or lower')
        size = int(input('Enter size of lists to be sorted (<=1000): '))

    arr = gen_arr(size)
    arr1 = copy.deepcopy(arr)
    arr2 = copy.deepcopy(arr)

    time1 = run_sort_timing(sorters[sorter_1], arr)
    time2 = run_sort_timing(sorters[sorter_2], arr)


    # ---------------- Visualization ----------------
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle('Sorting Algorithm Comparison')

    bar_rects1 = ax1.bar(range(size), arr1, align="edge", color='cornflowerblue')
    ax1.set_xlim(0, size)
    ax1.set_ylim(0, 10000)
    ax1.set_title(f'{sorter_1} Sort\nTime: {time1:.4f} sec')

    bar_rects2 = ax2.bar(range(size), arr2, align="edge", color='orange')
    ax2.set_xlim(0, size)
    ax2.set_ylim(0, 10000)
    ax2.set_title(f'{sorter_2} Sort\nTime: {time2:.4f} sec')

    anim1 = animation.FuncAnimation(
        fig, update_bars, fargs=(bar_rects1, 'cornflowerblue', 'red'),
        frames=sorters[sorter_1](arr1), interval=50, blit=True, repeat=False, cache_frame_data=False
    )
    anim2 = animation.FuncAnimation(
        fig, update_bars, fargs=(bar_rects2, 'orange', 'red'),
        frames=sorters[sorter_2](arr2), interval=50, blit=True, repeat=False, cache_frame_data=False
    )

    plt.tight_layout()
    plt.show()

    print('Sorting complete!')
    print(f"{sorter_1} Sort Time: {time1:.4f} seconds")
    print(f"{sorter_2} Sort Time: {time2:.4f} seconds")
