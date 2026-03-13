def heap_sort(array):
    
    n = len(array)

    for start in range((n - 2) // 2, -1, -1):
        sift_down(array, start, n - 1)

    for end in range(n - 1, 0, -1):
        array[0], array[end] = array[end], array[0]
        sift_down(array, 0, end - 1)