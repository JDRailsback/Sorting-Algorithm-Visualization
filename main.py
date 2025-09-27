import copy
import time
import numpy as np
from sorting_algorithms import sorters
from visualizer import visualize_sorting_comparison

def gen_arr(size):
    return [np.random.randint(0, 10000) for _ in range(size)]

def run_sort_timing(sorter_func, arr):
    arr_copy = copy.deepcopy(arr)
    start = time.perf_counter()
    for _ in sorter_func(arr_copy):
        pass
    return time.perf_counter() - start

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

    visualize_sorting_comparison(sorters[sorter_1], sorters[sorter_2], arr1, arr2, time1, time2)

    print('Sorting complete!')
    print(f"{sorter_1} Sort Time: {time1:.4f} seconds")
    print(f"{sorter_2} Sort Time: {time2:.4f} seconds")
