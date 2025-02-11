# Square
for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()

#Left Pyramid
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# Number Left Pyramid
for i in range(1, 6):
    for j in range(1, i):
        print(j, end=" ")
    print()

# Number Left Pyramid Row
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()
# Reverse star pyramid
for i in range(5, 0 , -1):
    for j in range(i):
        print("*", end=" ")
    print()
# Reverse number pyramid
for i in range(6, 0, -1):
    for j in range(1, i):
        print(j, end=" ")
    print()
# Star Pyramid
for i in range(1, 5 + 1):
    for j in range(5 - i):
        print(" ", end="")  
    
    for k in range(2 * i - 1):
        print("*", end="")  
    
    print() 
# Reverse Star Pyramid
for i in range(5,0 ,-1):
    for j in range(5 - i):
        print(" ", end="")  
    
    for k in range(2 * i - 1):
        print("*", end="")  
    
    print() 

# Flip left pyramid
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(6,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()
# Binary pyramid
for i in range(1, 5+1):
    start = i % 2
    for j in range(i):
        print(start, end="  ")
        start = 1- start
    print()
#Inside pyramid
for i in range(1, 5+1):
    for j in range(1 , i+1):
        print(j, end=" ")
    spaces = 2 * (5 - i)
    print("  " * spaces, end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# Increasing count pyramid
num = 1
for i in range(5):
    for j in range(1,i):
        print(num, end=" ")
        num = 1 + num
    print()

# Inside diamond
for i in range(5,0 ,-1):
    for j in range(1 , i+1):
        print(j, end=" ")
    spaces = 2 * (5 - i)
    print("  " * spaces, end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
for i in range(1, 5+1):
    for j in range(1 , i+1):
        print(j, end=" ")
    spaces = 2 * (5 - i)
    print("  " * spaces, end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
# symmetry
for i in range(1, 5+1):
    for j in range(1 , i+1):
        print(j, end=" ")
    spaces = 2 * (5 - i)
    print("  " * spaces, end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
for i in range(5,0 ,-1):
    for j in range(1 , i+1):
        print(j, end=" ")
    spaces = 2 * (5 - i)
    print("  " * spaces, end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
# Making Square

  ****
  *  *
  *  *
  ****  
