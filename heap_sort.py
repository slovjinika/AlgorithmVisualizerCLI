import time
from colorama import Back, Back, Style

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    # Подсветка элемента, который мы "просеиваем"
    #print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == i else str(x) for i, x in enumerate(arr))}")
    #time.sleep(0.1)

    if l < n and arr[i] < arr[l]:
        largest = l
        # Подсветка сравниваемых элементов
        #print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == i or i == l else str(x) for i, x in enumerate(arr))}")
        #time.sleep(0.1)

    if r < n and arr[largest] < arr[r]:
        largest = r
        # Подсветка сравниваемых элементов
        print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == largest or i == r else str(x) for i, x in enumerate(arr))}")
        time.sleep(0.1)

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Подсветка элементов, участвующих в обмене
        #print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == i or i == largest else str(x) for i, x in enumerate(arr))}")
        #time.sleep(0.1)
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        # Подсветка элементов, участвующих в обмене
        #print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == 0 or i == i else str(x) for i, x in enumerate(arr))}")
        #time.sleep(0.1)
        heapify(arr, i, 0)

array = ['M', 'X', 'C', 'G', 'U', 'I', 'K', 'O', 'B', 'Q', 'D', 'R', 'T', 'H', 'Y', 'S', 'P', 'F', 'L', 'N', 'E', 'W', 'V', 'J', 'Z', 'A']
#print(f"{' '.join(array)}")
#print(f"\033[31m{' '.join(array)}\033[0m")

start_time = time.time()
heapSort(array)
end_time = time.time()

#print(f"{' '.join(array)}")
print(f"\033[32m{' '.join(array)}\033[0m")
print(f"---------------------------------------------------")
elapsed_time = end_time - start_time

if elapsed_time >= 60:
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print(f"{minutes} minutes {seconds} seconds")
else:
    print(f"{elapsed_time:.2f} seconds")

