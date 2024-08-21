import time
from colorama import Back, Back, Style

def counting_sort(array):
    max_value = max(array)
    count = [0] * (max_value + 1)  # Массив для подсчета вхождений

    for x in array:
        count[x] += 1

    sorted_array = []
    for i in range(len(count)):
        for j in range(count[i]):
            sorted_array.append(i)
            print(f"{' '.join(Back.RED + str(chr(x)) + Back.RESET if x == i else str(chr(x)) for x in sorted_array)}")  # Подсветка
            time.sleep(0.1)

    return sorted_array

array = ['M', 'X', 'C', 'G', 'U', 'I', 'K', 'O', 'B', 'Q', 'D', 'R', 'T', 'H', 'Y', 'S', 'P', 'F', 'L', 'N', 'E', 'W', 'V', 'J', 'Z', 'A']
numbers = [ord(x) for x in array]  # Преобразуем строки в коды ASCII

start_time = time.time()
sorted_array = counting_sort(numbers)
end_time = time.time()

print(f"\033[32m{' '.join(chr(x) for x in sorted_array)}\033[0m")  # Подсвечиваем финальный результат
#print(f"Time: {end_time - start_time:.4f} seconds")
print(f"---------------------------------------------------")
elapsed_time = end_time - start_time

if elapsed_time >= 60:
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print(f"{minutes} minutes {seconds} seconds")
else:
    print(f"{elapsed_time:.2f} seconds")
