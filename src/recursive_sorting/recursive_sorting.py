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
    # First, we determine a starting index for the "right" half of the array
    start2 = mid + 1

    # Next, we write a while loop that will run until we have gone through one or both sides of the array
    while (start <= mid and start2 <= end):
        # The first thing we check in the while loop is whether the "left" and "right" elements we're looking at are already sorted (smaller on left, larger on right), and if they are, we increment the start index on the "left" array and go through the loop again
        if (arr[start] <= arr[start2]):
            start += 1
        else:
            # If the "right" element is greater than the "left" element, we set variables to point at the value and index of the "right" element that we are looking at
            value, index = arr[start2], start2

            # Then we write a while loop that will stop when the current index is equivalent to the start index
            while (index is not start):
                # During each loop, we are setting the value at the current index to the value at the index to the left of it, slowly moving the value to the right
                arr[index] = arr[index - 1]
                index -= 1

            # Once the element has been moved to the left enough, we
            arr[start] = value

            # Finally, we increment each of the index variables so we can traverse through the array
            start += 1
            mid += 1
            start2 += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # write an if statement to check if the left index is less than the right index, so the function will run until the array is broken down into single element arrays, as the left index will then equal the right index
    if (l < r):
        # If l < r, then we set a variable to the middle index
        middle = (l + r) // 2

        # Next, we recursively call merge_sort_in_place() on the "left" side of the array until l >= r, at which point we start backtracking through the stack to hit the "right" side of each array
        merge_sort_in_place(arr, l, middle)
        merge_sort_in_place(arr, middle + 1, r)

        # Once we have split an array into single element arrays, we call the helper function merge_in_place() and pass it
        merge_in_place(arr, l, middle, r)
        # print(arr)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
