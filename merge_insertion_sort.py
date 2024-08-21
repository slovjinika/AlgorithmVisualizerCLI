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

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    i = 0
    j = 0
    k = l
    comparisons = 0
    swaps = 0
    while i < n1 and j < n2:
        comparisons += 1
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            swaps += 1
        k += 1
        print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == k - 1 or j == k - 1 else str(x) for i, x in enumerate(arr))}")  # Подсвечиваем активные элементы
        time.sleep(0.1)
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == k - 1 else str(x) for i, x in enumerate(arr))}")  # Подсвечиваем активные элементы
        time.sleep(0.1)
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        #print(f"{' '.join(Back.RED + str(x) + Back.RESET if j == k - 1 else str(x) for i, x in enumerate(arr))}")  # Подсвечиваем активные элементы
        #time.sleep(0.1)
    return comparisons, swaps

def merge_insertion_sort(arr, l, r):
    comparisons = 0
    swaps = 0
    if l < r:
        m = (l + r) // 2
        comparisons_left, swaps_left = merge_insertion_sort(arr, l, m)
        comparisons_right, swaps_right = merge_insertion_sort(arr, m + 1, r)
        comparisons_merge, swaps_merge = merge(arr, l, m, r)
        comparisons += comparisons_left + comparisons_right + comparisons_merge
        swaps += swaps_left + swaps_right + swaps_merge
    return comparisons, swaps

array = ['M', 'X', 'C', 'G', 'U', 'I', 'K', 'O', 'B', 'Q', 'D', 'R', 'T', 'H', 'Y', 'S', 'P', 'F', 'L', 'N', 'E', 'W', 'V', 'J', 'Z', 'A']
#print(f"{' '.join(array)}")
#print(f"\033[31m{' '.join(array)}\033[0m")

start_time = time.time()
total_comparisons, total_swaps = merge_insertion_sort(array, 0, len(array) - 1)
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
