# Functions are set of code that do something for you
# Functions are use to increase readability

#Function without para and without return

def greet():
    print("hello bros")

greet()

#Function without para and  return

def getpi():
    return 3.14
pie = getpi()
print(pie)

#Function With Parameters and Without Return Value

def getname(name):
    print(f"your {name}")

getname("chetanya")

#Function With Parameters and With Return Value

def add(a, b):
    return a + b

result = add(3, 5)
print(result)

# Lambda Function (One-line Anonymous Function)

square = lambda x: x * x
print(square(4))

