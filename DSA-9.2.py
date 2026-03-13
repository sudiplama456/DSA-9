def sift_down(array, start, end):
    
    
    root = start

    while 2 * root + 1 <= end:
        child = 2 * root + 1
        swap = root

        if array[swap] < array[child]:
            swap = child

        if child + 1 <= end and array[swap] < array[child + 1]:
            swap = child + 1

        if swap == root:
            return
        else:
            array[root], array[swap] = array[swap], array[root]
            root = swap