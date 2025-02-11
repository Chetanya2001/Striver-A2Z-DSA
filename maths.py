num = 567008
rev = 0
while num > 0:
    last = num % 10
    num //= 10
    rev = (rev * 10) + last
print(rev)