arr = [1,2,3,6,7,9,12,15,8 , 13]
def findMax(arr):
    largest = arr[0]
    for i in arr:
        if largest < i:
            largest = i
    return largest
print(findMax(arr))

def SecondLargest(arr):
    largest = arr[0]
    second = arr[1]
    for num in arr:
        if largest < num:
            second = largest
            largest = num
        if num > second and num < largest:
            second = num
    return second
print(SecondLargest(arr))
sorted = [1,1,1,2,2,3,3,4,4,5,5,5,6,6,6,6]
def RemoveDuplicateOrFindUnique(sorted):
    unique = [sorted[0]]
    for i in range(1, len(sorted)):
        if sorted[i] != sorted[i - 1]:
            unique.append(sorted[i])
    return unique



print(RemoveDuplicateOrFindUnique(sorted))

        