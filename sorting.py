#Selection Sort
arr = [13,46,24,52,20,9]
for i in range(len(arr) -1):
    mini = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[mini]:
            mini = j
    arr[i], arr[mini] = arr[mini] , arr[i]
print(arr)
# Bubble Sort
n = len(arr)
for i in range(n):
    for j in range(0, n - i -1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)
#  Insertion Sort
for i in range(1 , n):
    key = arr[i]
    j = i - 1
    while j > 0 and arr[j] > key:
        arr[j+ 1] = arr[j]
        j = j - 1
    arr[j+1] = key
print(arr)

# Merge Sort Implementation
def mergeSort(arr, low, high):
    if low >= high:
        return
    
    # Correct calculation of mid
    mid = (low + high) // 2
    
    # Recursive calls
    mergeSort(arr, low, mid)
    mergeSort(arr, mid + 1, high)
    
    # Merge the two halves
    merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    # Merge the two halves into temp
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # Add the remaining elements from the left half
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # Add the remaining elements from the right half
    while right <= high:
        temp.append(arr[right])
        right += 1

    # Copy the sorted elements back to the original array
    for i in range(len(temp)):
        arr[low + i] = temp[i]


print(mergeSort(arr, 0, len(arr) - 1))
print(arr)
#Quick Sort
def QuickSort(array):
    if len(array) <= 1:  # Base case: array is already sorted
        return array
    
    pivot = array[0]  # Choose the first element as the pivot
    
    # Correct partitioning
    smaller = [x for x in array[1:] if x <= pivot]  # Use elements after pivot
    greater = [x for x in array[1:] if x > pivot]
    
    # Recursive calls and combine results
    return QuickSort(smaller) + [pivot] + QuickSort(greater)

print(QuickSort(arr))  # Output: [2, 3, 4, 5, 6, 7, 8]
