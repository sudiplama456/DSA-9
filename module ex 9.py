import random
import time

data_size = 300
original_data = [random.randint(1, 1000) for _ in range(data_size)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def run_test(name, sort_func, data):
    arr = data.copy()
    
    start_time = time.perf_counter()
    sorted_arr = sort_func(arr)
    end_time = time.perf_counter()
    
    print(f"--- {name} ---")
    print(f"Time: {end_time - start_time:.6f} sec")
    print(f"Data: {sorted_arr}\n")

if __name__ == "__main__":
    print(f"Running sorts on {data_size} elements...\n")
    
    run_test("Bubble Sort", bubble_sort, original_data)
    run_test("Insertion Sort", insertion_sort, original_data)
    run_test("Quick Sort", quick_sort, original_data)