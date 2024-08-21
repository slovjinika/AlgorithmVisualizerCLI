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

def tree_sort(array):
    comparisons = 0
    swaps = 0
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        comparisons += 1
        while j >= 0 and key < array[j]:
            comparisons += 1
            array[j + 1] = array[j]
            j -= 1
            swaps += 1
            print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == j + 1 or i == j else str(x) for i, x in enumerate(array))}")  # Подсвечиваем j + 1 и j
            time.sleep(0.1)
        array[j + 1] = key
    return comparisons, swaps


array = ['M', 'X', 'C', 'G', 'U', 'I', 'K', 'O', 'B', 'Q', 'D', 'R', 'T', 'H', 'Y', 'S', 'P', 'F', 'L', 'N', 'E', 'W', 'V', 'J', 'Z', 'A']
#print(f"{' '.join(array)}")
#print(f"\033[31m{' '.join(array)}\033[0m")

start_time = time.time()
total_comparisons, total_swaps = tree_sort(array)
end_time = time.time()

#print(f"{' '.join(array)}")
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
