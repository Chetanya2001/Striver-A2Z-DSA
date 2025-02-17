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
