import time
from colorama import Back, Back, Style

def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    while (swapped == True):
        swapped = False
        for i in range(start, end):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
                print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == j or i + 1 == j else str(x) for j, x in enumerate(a))}")  # Исправлено условие
                time.sleep(0.1)
        if (swapped == False):
            break
        swapped = False
        end = end - 1
        for i in range(end - 1, start - 1, -1):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
                print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == j or i + 1 == j else str(x) for j, x in enumerate(a))}")  # Исправлено условие
                time.sleep(0.1)
        start = start + 1

array = ['M', 'X', 'C', 'G', 'U', 'I', 'K', 'O', 'B', 'Q', 'D', 'R', 'T', 'H', 'Y', 'S', 'P', 'F', 'L', 'N', 'E', 'W', 'V', 'J', 'Z', 'A']
#print(f"{' '.join(array)}")

start_time = time.time()
cocktailSort(array)
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

