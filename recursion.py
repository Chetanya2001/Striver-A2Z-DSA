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



