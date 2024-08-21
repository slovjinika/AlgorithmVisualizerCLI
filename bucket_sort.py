import time
from colorama import Back, Style

def bucket_sort(array):
    n = len(array)
    buckets = [[] for _ in range(n)]
    comparisons = 0
    swaps = 0

    # Распределение элементов по корзинам
    for i, element in enumerate(array):
        bucket_index = min(int(n * (ord(element) - ord('A')) / (ord('Z') - ord('A'))), n - 1)
        buckets[bucket_index].append(element)
        print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == bucket_index else str(x) for i, x in enumerate(array))}")  # Подсветка корзины
        time.sleep(0.1)

    # Сортировка каждой корзины (в данном случае используется вставка)
    for i, bucket in enumerate(buckets):
        bucket.sort()  # Сортировка корзины
        print(f"{' '.join(Back.RED + str(x) + Back.RESET if i == bucket_index else str(x) for i, x in enumerate(array))}")  # Подсветка корзины
        time.sleep(0.1)

    # Объединение отсортированных корзин
    sorted_array = []
    for bucket in buckets:
        for element in bucket:
            sorted_array.append(element)
            print(f"{' '.join(Back.RED + str(x) + Back.RESET if x in sorted_array else str(x) for i, x in enumerate(array))}")
            time.sleep(0.1)

    return sorted_array, comparisons, swaps

array = ['M', 'X', 'C', 'G', 'U', 'I', 'K', 'O', 'B', 'Q', 'D', 'R', 'T', 'H', 'Y', 'S', 'P', 'F', 'L', 'N', 'E', 'W', 'V', 'J', 'Z', 'A']

start_time = time.time()
sorted_array, total_comparisons, total_swaps = bucket_sort(array)
end_time = time.time()

print(f"\033[32m{' '.join(sorted_array)}\033[0m")

print(f"---------------------------------------------------")
elapsed_time = end_time - start_time

if elapsed_time >= 60:
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print(f"{minutes} minutes {seconds} seconds")
else:
    print(f"{elapsed_time:.2f} seconds")

