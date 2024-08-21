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

def slow_sort(array, start, end):
    if start >= end:
        return 0, 0, 0
    comparisons = 0
    swaps = 0
    for i in range(start, end + 1):
        for j in range(i + 1, end + 1):
            comparisons += 1
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                swaps += 1
                # Подсвечиваем только j-й элемент:
                print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == j else str(x) for i, x in enumerate(array))}") 
                time.sleep(0.1)
    return comparisons, swaps, end

array = ['M', 'X', 'C', 'G', 'U', 'I', 'K', 'O', 'B', 'Q', 'D', 'R', 'T', 'H', 'Y', 'S', 'P', 'F', 'L', 'N', 'E', 'W', 'V', 'J', 'Z', 'A']

start_time = time.time()
total_comparisons, total_swaps, _ = slow_sort(array, 0, len(array) - 1)
end_time = time.time()

print(f"\033[32m{' '.join(array)}\033[0m")

#print(f"---------------------------------------------------")
#print(f"Swaps: {total_swaps}")
#print(f"Comparisons: {total_comparisons}")

print(f"---------------------------------------------------")
elapsed_time = end_time - start_time

if elapsed_time >= 60:
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print(f"{minutes} minutes {seconds} seconds")
else:
    print(f"{elapsed_time:.2f} seconds")