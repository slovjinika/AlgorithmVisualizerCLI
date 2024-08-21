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

def stoogesort(arr, l, h):
    if l >= h:
        return
    if arr[l] > arr[h]:
        t = arr[l]
        arr[l] = arr[h]
        arr[h] = t
    if h - l + 1 > 2:
        t = (int)((h - l + 1) / 3)
        print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == l or i == h else str(x) for i, x in enumerate(arr))}")
        time.sleep(0.1)
        stoogesort(arr, l, (h - t))
        print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == l + t or i == h else str(x) for i, x in enumerate(arr))}")
        time.sleep(0.1)
        stoogesort(arr, l + t, (h))
        print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == l or i == (h - t) else str(x) for i, x in enumerate(arr))}")
        time.sleep(0.1)
        stoogesort(arr, l, (h - t))

array = ['M', 'X', 'C', 'G', 'U', 'I', 'K', 'O', 'B', 'Q', 'D', 'R', 'T', 'H', 'Y', 'S', 'P', 'F', 'L', 'N', 'E', 'W', 'V', 'J', 'Z', 'A']

start_time = time.time()
stoogesort(array, 0, len(array) - 1)
end_time = time.time()

print(f"\033[32m{' '.join(array)}\033[0m")

print(f"---------------------------------------------------")
elapsed_time = end_time - start_time

if elapsed_time >= 60:
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print(f"{minutes} minutes {seconds} seconds")
else:
    print(f"{elapsed_time:.2f} seconds")
