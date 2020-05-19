# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    print(f"MERGING:{arrA} - {arrB}")
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements  # Allocating memory

    # Initializing pointers to the font of A and B arrays
    a = 0
    b = 0

    # Compare the first elements of A and B
    # Copy the smallest to merged_arr
    for i in range(elements):
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    print(f"SORTING: {arr}")
    # Base case: If the array is empty or length 1, return
    if len(arr) <= 1:
        return arr
# Split arrays in half
    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:]
# Sort each half
    left = merge_sort(left)
    right = merge_sort(right)
# Merge them back together
    return merge(left, right)


arr = [2, 9, 7, 0, 8, 3, 1, 4, 6, 5]
print(merge_sort(arr))


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
