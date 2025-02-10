name = "chetanya"
i = 0
while i < len(name):
    print(name[i])
    i += 1
Two_D_array = [[1,2,3],
               [4,5,6],
               [7,8,9]]
j = 0

while j < len(Two_D_array):
    k = 0
    while k < len(Two_D_array):
        print(Two_D_array[j][k])
        k += 1
    j += 1


#Do while loop
while True:
    num = int(input("enter a number :"))
    if num > 0:
        break
    print("Try again")
