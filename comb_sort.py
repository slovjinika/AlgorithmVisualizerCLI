import time
from colorama import Back, Back, Style

def comb_sort(arr):
    length = len(arr)
    shrink = 1.3
    gap = length
    sorted = False
    while not sorted:
        gap = int(gap/shrink)
        if gap <= 1:
            sorted = True
            gap = 1
        for i in range(length-gap):
            sm = gap + i
            if arr[i] > arr[sm]:
                arr[i], arr[sm] = arr[sm], arr[i]
                # Подсвечиваем только элементы i и sm
                print(f"{' '.join(Back.RED + str(x) + Back.RESET if j == i or j == sm else str(x) for j, x in enumerate(arr))}")
                time.sleep(0.1)
                sorted = False

array = ['M', 'X', 'C', 'G', 'U', 'I', 'K', 'O', 'B', 'Q', 'D', 'R', 'T', 'H', 'Y', 'S', 'P', 'F', 'L', 'N', 'E', 'W', 'V', 'J', 'Z', 'A']

start_time = time.time()
comb_sort(array)
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
