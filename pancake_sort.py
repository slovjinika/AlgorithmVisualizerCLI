import time
from colorama import Back, Back, Style

def flip(arr, k):
    left = 0
    while left < k:
        arr[left], arr[k] = arr[k], arr[left]
        print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == left or i == k else str(x) for i, x in enumerate(arr))}")  # Подсвечиваем left и k
        time.sleep(0.1)
        k -= 1
        left += 1

def max_index(arr, k):
    index = 0
    for i in range(k):
        if arr[i] > arr[index]:
            index = i
    return index

def pancake_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    while n > 1:
        comparisons += n - 1
        maxdex = max_index(arr, n)
        swaps += maxdex
        if maxdex != n - 1:
            flip(arr, maxdex)
            swaps += n - 1
            print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == maxdex or i == n-1 else str(x) for i, x in enumerate(arr))}")  # Подсвечиваем maxdex и n-1
            time.sleep(0.1)
            flip(arr, n - 1)
        n -= 1
    # Дополнительная проверка для последнего элемента
    if n == 1:
        if arr[0] > arr[1]:
            flip(arr, 0)
    return comparisons, swaps

array = ['M', 'X', 'C', 'G', 'U', 'I', 'K', 'O', 'B', 'Q', 'D', 'R', 'T', 'H', 'Y', 'S', 'P', 'F', 'L', 'N', 'E', 'W', 'V', 'J', 'Z', 'A']
#print(f"{' '.join(array)}")

start_time = time.time()
total_comparisons, total_swaps = pancake_sort(array)
end_time = time.time()

print(f"\033[32m{' '.join(array)}\033[0m")

#print(f"---------------------------------------------------")
#print(f"Swaps: {total_swaps}")
#print(f"Comparisons: {total_comparisons}")
#print(f"Time: {end_time - start_time:.4f} seconds")
print(f"---------------------------------------------------")
elapsed_time = end_time - start_time

if elapsed_time >= 60:
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print(f"{minutes} minutes {seconds} seconds")
else:
    print(f"{elapsed_time:.2f} seconds")
