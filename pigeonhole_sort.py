import time
from colorama import Back, Back, Style

def pigeonhole_sort(array):
    """Сортировка методом "голубиных отверстий" с подсвечиванием."""
    # Преобразуем буквы в ординалы
    array = [ord(x) for x in array]  # Преобразуем буквы в ординалы
    min_value = min(array)
    max_value = max(array)
    range_size = max_value - min_value + 1
    pigeonholes = [0] * range_size

    comparisons = 0  # Счетчик сравнений
    swaps = 0  # Счетчик перестановок

    # Распределение элементов в "голубиные отверстия"
    for i in range(len(array)):
        comparisons += 1
        pigeonholes[array[i] - min_value] += 1

    # Создание отсортированного массива
    index = 0
    for i in range(range_size):
        for j in range(pigeonholes[i]):
            comparisons += 1
            array[index] = i + min_value
            index += 1
            # Преобразуем ординалы обратно в буквы
            array = [chr(x) for x in array]  # Преобразуем ординалы обратно в буквы
            print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == index - 1 else str(x) for i, x in enumerate(array))}")  # Подсвечиваем активный элемент
            time.sleep(0.1)
            # Преобразуем буквы обратно в ординалы
            array = [ord(x) for x in array]  # Преобразуем буквы обратно в ординалы

    # Преобразуем ординалы обратно в буквы
    array = [chr(x) for x in array]
    return array, comparisons, swaps

array = ['M', 'X', 'C', 'G', 'U', 'I', 'K', 'O', 'B', 'Q', 'D', 'R', 'T', 'H', 'Y', 'S', 'P', 'F', 'L', 'N', 'E', 'W', 'V', 'J', 'Z', 'A']
# print(f"{' '.join(array)}")

start_time = time.time()
sorted_array, total_comparisons, total_swaps = pigeonhole_sort(array.copy())
end_time = time.time()

# print(f"{' '.join(array)}")
print(f"\033[32m{' '.join(sorted_array)}\033[0m")

# print(f"---------------------------------------------------")
# print(f"Swaps: {total_swaps}")
# print(f"Comparisons: {total_comparisons}")
print(f"---------------------------------------------------")
elapsed_time = end_time - start_time

if elapsed_time >= 60:
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print(f"{minutes} minutes {seconds} seconds")
else:
    print(f"{elapsed_time:.2f} seconds")
