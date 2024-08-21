import time
from colorama import Back, Back, Style

def gnomeSort( arr, n):
  index = 0
  while index < n:
    if index == 0:
      index = index + 1
    if arr[index] >= arr[index - 1]:
      index = index + 1
    else:
      arr[index], arr[index-1] = arr[index-1], arr[index]
      print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == index or i == index - 1 else str(x) for i, x in enumerate(arr))}")  # Подсвечиваем index и index-1
      time.sleep(0.1)
      index = index - 1

array = ['M', 'X', 'C', 'G', 'U', 'I', 'K', 'O', 'B', 'Q', 'D', 'R', 'T', 'H', 'Y', 'S', 'P', 'F', 'L', 'N', 'E', 'W', 'V', 'J', 'Z', 'A']
#print(f"{' '.join(array)}")

start_time = time.time()
gnomeSort(array, len(array))
end_time = time.time()

print(f"\033[32m{' '.join(array)}\033[0m") 
#print(f"---------------------------------------------------")
#print(f"Time: {end_time - start_time:.4f} seconds")
print(f"---------------------------------------------------")
elapsed_time = end_time - start_time

if elapsed_time >= 60:
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print(f"{minutes} minutes {seconds} seconds")
else:
    print(f"{elapsed_time:.2f} seconds")
