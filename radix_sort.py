import time
from colorama import Back, Back, Style

def countingSort(arr, exp1, comparisons, swaps):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (26) # 26 букв в английском алфавите
    for i in range(0, n):
        index = ord(arr[i]) - ord('A') # Получение ASCII-кода буквы, вычитаем ASCII-код 'A'
        comparisons += 1
        count[index] += 1

    for i in range(1, 26):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = ord(arr[i]) - ord('A')
        comparisons += 1
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == count[index] - 1 else str(x) for i, x in enumerate(arr))}")
        time.sleep(0.1)
        i -= 1

    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
        print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == count[index] - 1 else str(x) for i, x in enumerate(arr))}")
        time.sleep(0.1)
        comparisons += 1

    return comparisons, swaps

def radixSort(arr):
    comparisons = 0
    swaps = 0
    exp = 1  # Начинаем с разряда единиц
    while exp <= 100:  # 100 для максимального ASCII-кода (90)
        comparisons, swaps = countingSort(arr, exp, comparisons, swaps)
        exp *= 10
    return comparisons, swaps

# Пример использования
array = ['M', 'X', 'C', 'G', 'U', 'I', 'K', 'O', 'B', 'Q', 'D', 'R', 'T', 'H', 'Y', 'S', 'P', 'F', 'L', 'N', 'E', 'W', 'V', 'J', 'Z', 'A']
#print(f"{' '.join(str(x) for x in array)}")

start_time = time.time()
total_comparisons, total_swaps = radixSort(array)
end_time = time.time()

#print(f"{' '.join(Back.GREEN + str(x) + Back.RESET for x in array)}")
print(f"\033[32m{' '.join(array)}\033[0m")
#print(f"---------------------------------------------------")
#print(f"Swaps: {total_swaps}")
#print(f"Comparisons: {total_comparisons}")
#print(f"{end_time - start_time:.4f} seconds")

print(f"---------------------------------------------------")
elapsed_time = end_time - start_time

if elapsed_time >= 60:
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print(f"{minutes} minutes {seconds} seconds")
else:
    print(f"{elapsed_time:.2f} seconds")
