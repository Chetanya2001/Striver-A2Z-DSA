age = int(input("Enter your age: "))

def operation(age):
    match age:
        case _ if age > 18:
            return "You are an adult."
        case _ if age == 18:
            return "You just became an adult!"
        case _:
            return "You are a minor."

print(operation(age))


