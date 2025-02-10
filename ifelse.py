age = int(input("Enter your age: "))
if age > 24:
    print("You are a man")
elif age > 18 and age < 24:
    print("You are an adult")
else:
    print("You are under 18")

marks = int(input("Enter your marks : "))
if marks >= 90:
    print("S grade")
elif marks >= 80 and marks < 90:
    print("A grade")
elif marks >= 70 and marks < 80:
    print("B grade")
elif marks >=60 and marks < 70:
    print("C grade")
elif marks >= 50 and marks < 60:
    print("D grade")
elif marks >= 40 and marks < 50:
    print("E grade")
else:
    print("Fail")
