import time
from colorama import Back, Back, Style

def odd_even_sort(L):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, len(L)-1, 2):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                sorted = False
                print(f"{' '.join(Back.RED + str(x) + Back.RESET if j == i or j == i+1 else str(x) for j, x in enumerate(L))}") # Изменено: j используется для индексации элементов в L
                time.sleep(0.1) 

        for i in range(0, len(L)-1, 2):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                sorted = False
                print(f"{' '.join(Back.RED + str(x) + Back.RESET if j == i or j == i+1 else str(x) for j, x in enumerate(L))}") # Изменено: j используется для индексации элементов в L
                time.sleep(0.1) 

array = ['M', 'X', 'C', 'G', 'U', 'I', 'K', 'O', 'B', 'Q', 'D', 'R', 'T', 'H', 'Y', 'S', 'P', 'F', 'L', 'N', 'E', 'W', 'V', 'J', 'Z', 'A']
#print(f"{' '.join(array)}")

start_time = time.time()
odd_even_sort(array)
end_time = time.time()

print(f"\033[32m{' '.join(array)}\033[0m")  # Вывод отсортированного массива зеленым
#print(f"Время выполнения: {end_time - start_time:.4f} секунд")

print(f"---------------------------------------------------")
elapsed_time = end_time - start_time

if elapsed_time >= 60:
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print(f"{minutes} minutes {seconds} seconds")
else:
    print(f"{elapsed_time:.2f} seconds")
