import time
from colorama import Back, Back, Style

def mergeSort(arr):
    comparisons = 0
    swaps = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        comparisons += mergeSort(L)[0]
        swaps += mergeSort(L)[1]
        comparisons += mergeSort(R)[0]
        swaps += mergeSort(R)[1]
        i = j = k = 0
        while i < len(L) and j < len(R):
            comparisons += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == k or j == k else str(x) for i, x in enumerate(arr))}")
            time.sleep(0.1)  # Задержка для анимации
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            #print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == k else str(x) for i, x in enumerate(arr))}")
            #time.sleep(0.1)  # Задержка для анимации
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            #print(f"{' '.join(Back.RED + str(x) + Back.RESET if j == k else str(x) for i, x in enumerate(arr))}")
            #time.sleep(0.1)  # Задержка для анимации
    return comparisons, swaps


array = ['M', 'X', 'C', 'G', 'U', 'I', 'K', 'O', 'B', 'Q', 'D', 'R', 'T', 'H', 'Y', 'S', 'P', 'F', 'L', 'N', 'E', 'W', 'V', 'J', 'Z', 'A']
# print(f"{' '.join(array)}")
# print(f"\033[31m{' '.join(array)}\033[0m")

start_time = time.time()
total_comparisons, total_swaps = mergeSort(array)
end_time = time.time()

# print(f"{' '.join(array)}")
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
