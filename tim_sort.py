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

def tim_sort(array):
    """
    Реализация алгоритма сортировки TimSort.
    """
    min_run = 32  # Минимальная длина подпоследовательности
    n = len(array)
    comparisons = 0  # Счетчик сравнений
    swaps = 0  # Счетчик перестановок

    # 1. Разделение на подпоследовательности
    for start in range(0, n, min_run):
        end = min(start + min_run, n)
        # Сортировка каждой подпоследовательности с помощью вставки
        for i in range(start + 1, end):
            j = i
            while j > start and array[j - 1] > array[j]:
                comparisons += 1
                array[j - 1], array[j] = array[j], array[j - 1]
                swaps += 1
                print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == j - 1 or i == j else str(x) for i, x in enumerate(array))}")
                time.sleep(0.1)
                j -= 1

    # 2. Слияние подпоследовательностей
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size, n)
            right = min(left + 2 * size, n)
            # Слияние подпоследовательностей с использованием merge_sort
            merge_sort(array, left, mid, right, comparisons, swaps)
            size *= 2

    return comparisons, swaps

def merge_sort(array, left, mid, right, comparisons, swaps):
    """
    Слияние двух отсортированных подпоследовательностей.
    """
    n1 = mid - left
    n2 = right - mid
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    for i in range(0, n1):
        L[i] = array[left + i]
    for i in range(0, n2):
        R[i] = array[mid + i]
    L[n1] = float('inf')  # Сторожевой элемент для L
    R[n2] = float('inf')  # Сторожевой элемент для R
    i = 0
    j = 0
    for k in range(left, right):
        comparisons += 1
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == k else str(x) for i, x in enumerate(array))}")
        time.sleep(0.1)
    swaps += i + j - (mid - left) - (right - mid)


array = ['M', 'X', 'C', 'G', 'U', 'I', 'K', 'O', 'B', 'Q', 'D', 'R', 'T', 'H', 'Y', 'S', 'P', 'F', 'L', 'N', 'E', 'W', 'V', 'J', 'Z', 'A']
#print(f"{' '.join(array)}")
#print(f"033[31m{' '.join(array)}033[0m")

start_time = time.time()
total_comparisons, total_swaps = tim_sort(array)
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
