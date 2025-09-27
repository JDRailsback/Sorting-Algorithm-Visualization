import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sorting_algorithms import is_sorted

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

def visualize_sorting_comparison(sorter_1, sorter_2, arr1, arr2, time1, time2):
    size = len(arr1)
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
        frames=sorter_1(arr1), interval=50, blit=True, repeat=False, cache_frame_data=False
    )
    anim2 = animation.FuncAnimation(
        fig, update_bars, fargs=(bar_rects2, 'orange', 'red'),
        frames=sorter_2(arr2), interval=50, blit=True, repeat=False, cache_frame_data=False
    )

    plt.tight_layout()
    plt.show()