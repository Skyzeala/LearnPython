


#syntax and indentation?

# Booleans are values that are either True or False, stored as 1 and 0 respectively 

myBool = False
myInt = 0

print(myBool)
print(str(type(myBool)))

print(myBool == 0)
print(True == 1)


#if elif else





# This is a match statement, it takes an argument and tries to match it against each case given
# If a case matches the argument, it will run the subsequent code
# In other languages, this is often called a switch statement or switch-case statement

    
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 401 | 403 | 404:
            return "Not allowed"
        case _:
            return "Something's wrong with the internet"
        

point = (0,7)


match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

