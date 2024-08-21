import time
from colorama import Back, Back, Style

def selection_sort(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
        print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == min_idx or i == j else str(x) for i, x in enumerate(A))}")
        time.sleep(0.1)

# Пример использования:
array = ['M', 'X', 'C', 'G', 'U', 'I', 'K', 'O', 'B', 'Q', 'D', 'R', 'T', 'H', 'Y', 'S', 'P', 'F', 'L', 'N', 'E', 'W', 'V', 'J', 'Z', 'A']

start_time = time.time()
selection_sort(array)
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
