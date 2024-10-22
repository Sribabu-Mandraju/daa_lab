def merge_sort(arr):
    # Base case: a single element is already sorted
    if len(arr) <= 1:
        return arr
    
    # Step 1: Divide the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])   # Recursive call on the left half
    right_half = merge_sort(arr[mid:])  # Recursive call on the right half
    
    # Step 2: Conquer by merging the two halves
    return merge(left_half, right_half)

# Helper function to merge two sorted halves
def merge(left, right):
    sorted_arr = []
    i = j = 0
    
    # Compare elements from both halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    
    # If there are remaining elements in the left half, add them
    while i < len(left):
        sorted_arr.append(left[i])
        i += 1
    
    # If there are remaining elements in the right half, add them
    while j < len(right):
        sorted_arr.append(right[j])
        j += 1
    
    return sorted_arr

# Example usage
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
