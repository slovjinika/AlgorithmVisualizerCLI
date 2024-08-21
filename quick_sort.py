import time
from colorama import Back, Back, Style

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end
    comparisons = 0  # Счетчик сравнений
    swaps = 0  # Счетчик перестановок
    while True:
        comparisons += 1
        while low <= high and array[high] >= pivot:
            high = high - 1
            comparisons += 1
        comparisons += 1
        while low <= high and array[low] <= pivot:
            low = low + 1
            comparisons += 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
            swaps += 1
            print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == low or i == high else str(x) for i, x in enumerate(array))}")  # Подсвечиваем low и high
            time.sleep(0.1)
        else:
            break
    array[start], array[high] = array[high], array[start]
    swaps += 1
    print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == start or i == high else str(x) for i, x in enumerate(array))}")  # Подсвечиваем start и high
    time.sleep(0.1)
    return high, comparisons, swaps


def quick_sort(array, start, end):
    if start >= end:
        return 0, 0, 0
    p, comparisons, swaps = partition(array, start, end)
    left_comparisons, left_swaps, _ = quick_sort(array, start, p - 1)
    right_comparisons, right_swaps, _ = quick_sort(array, p + 1, end)
    return comparisons + left_comparisons + right_comparisons, swaps + left_swaps + right_swaps, p

array = ['M', 'X', 'C', 'G', 'U', 'I', 'K', 'O', 'B', 'Q', 'D', 'R', 'T', 'H', 'Y', 'S', 'P', 'F', 'L', 'N', 'E', 'W', 'V', 'J', 'Z', 'A']
#print(f"{' '.join(array)}")
#print(f"\033[31m{' '.join(array)}\033[0m")


start_time = time.time()
total_comparisons, total_swaps, _ = quick_sort(array, 0, len(array) - 1)
end_time = time.time()

#print(f"{' '.join(array)}")
print(f"\033[32m{' '.join(array)}\033[0m") 

print(f"---------------------------------------------------")
#print(f"Swaps: {total_swaps}")
#print(f"Comparisons: {total_comparisons}")

elapsed_time = end_time - start_time

if elapsed_time >= 60:
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print(f"{minutes} minutes {seconds} seconds")
else:
    print(f"{elapsed_time:.2f} seconds")

