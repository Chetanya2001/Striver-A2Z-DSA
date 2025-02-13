count = 0
def Counter():
    global count
    if count == 10:
        return 1
    print(count)
    count += 1
    return Counter() 

print(Counter())

#Basic Recursion Problems
# Printing Names
def Name(i ,n):
    if i == n:
        return
    print("Chetanya")
    return Name(i+1, n)
Name(0, 5)
# Print linearly 1 to N
def Printer(i, n ):
    if i == n + 1:
        return
    print(i)
    return Printer(i+1, n)
Printer(1, 7)

#  Print In Opposite number
def Opposite(n):
    if n == 0:
        return
    print(n)
    return Opposite(n - 1)
Opposite(7)
# Back Tracking
def Back(n):
    if n == 0:
        return
    Back(n - 1) 
    print(n)     

Back(7)
# N to 1
def backtrack(i, n):
    if i > n:
        return
    backtrack(i+1, n)
    print(i)

backtrack(1, 5)

# Sum first N numbers
sum = 0
def Sum(n):
    global sum
    if n == 0:
        return print(sum)
    sum += n
    return Sum(n - 1)
Sum(10)

# factorial

def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1) * n
print(factorial(3))

# Reverse An Array
def reverse(arr,l,r):
    if l >= r:
        return 
    arr[l], arr[r] = arr[r], arr[l]
    return reverse(arr, l+1, r-1)
array = [1,2,3,4,5,6]
reverse(array,0,len(array)- 1)
print(array)
        
# Fibonacci numbers
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(3))

    


