import time
from colorama import Back, Back, Style

def shellSort(arr):
    n = len(arr)
    gap = n // 2
    comparisons = 0  # Счетчик сравнений
    swaps = 0  # Счетчик перестановок
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                comparisons += 1
                arr[j] = arr[j - gap]
                j -= gap
                print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == j or i == j - gap else str(x) for i, x in enumerate(arr))}")  # Подсвечиваем j и j-gap
                time.sleep(0.1)
            comparisons += 1
            arr[j] = temp
            swaps += 1
            print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == j else str(x) for i, x in enumerate(arr))}")  # Подсвечиваем j
            time.sleep(0.1)
        gap //= 2
    return comparisons, swaps

array = ['M', 'X', 'C', 'G', 'U', 'I', 'K', 'O', 'B', 'Q', 'D', 'R', 'T', 'H', 'Y', 'S', 'P', 'F', 'L', 'N', 'E', 'W', 'V', 'J', 'Z', 'A']
#print(f"{' '.join(array)}")

start_time = time.time()
total_comparisons, total_swaps = shellSort(array)
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
