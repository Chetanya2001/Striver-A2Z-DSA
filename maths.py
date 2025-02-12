import math
# Reverse Number
num = 567008
rev = 0
while num > 0:
    last = num % 10
    num //= 10
    rev = (rev * 10) + last
print(rev)

# Palindrome Number
def isPalindrome(num):
    if num < 0:
        return False
    rev = 0
    dup = num
    while num > 0:
        rev = (rev * 10) + num % 10
        num //= 10
    return dup == rev
print(isPalindrome(121))

# Armstrong Number
def isArmstrong(n):
    digit = len(str(n))
    original = n 
    sum = 0
    while n > 0:
        last = n % 10
        sum = sum + pow(last, digit)
        n //= 10  
    if sum == original:
        print("YES, it is an Armstrong number")
    else:
        print("NO, it is not an Armstrong number")
isArmstrong(1634)
#Print All Divisors
def AllDivisors(number):
    divisor = []
    for i in range(1, int(math.sqrt(number))+ 1):
        if number % i == 0:
            divisor.append(i)
            if i != number // i:
                divisor.append(number//i)
    return divisor

print(AllDivisors(12))

def isPrime(number):
    divisor = []
    for i in range(1, int(math.sqrt(number))+ 1):
        if number % i == 0:
            divisor.append(i)
            if i != number // i:
                divisor.append(number//i)
    if len(divisor) == 2:
        return print("It is a prime")
    else:
        return print("It not a prime number")
isPrime(24)

def isGCD(x,y):
    divisor = []
    n =  x if x < y  else y
    for i in range(1, n):
        if x % i == 0 and y % i == 0:
            divisor.append(i)
    return max(divisor)
print(isGCD(9,12))

