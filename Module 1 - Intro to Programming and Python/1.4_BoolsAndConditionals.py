# Booleans are values that are either True or False, and can evaluate as 1 and 0 respectively if desired

my_bool = False
my_int = 0

print(my_bool)
print(str(type(my_bool)))

# You can check for eqivalency between two values using the == operator 
print(my_bool == False) # Is my_bool False? Yes, so we display True
print(my_bool != True) # Is my_bool NOT True? Yes, so we display True
print(True == 1) # True and False are equivalent to 1 and 0 respectively





# Code can be aggregated into what are called blocks
# In Python, blocks are indicated by indentation, which is typically 4 spaces or a tab
# Tabs and spaces cannot be intermixed, and may cause errors if done so accidentally
# VSCode and many other IDEs automatically convert tabs to 4 spaces to provide consistency
# You can learn more about typical Python coding style here
#     https://peps.python.org/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds

#if elif else

my_bool = False

# If statements will check a condition, if the condition is True it will execute the following block of code
if (5 > 0):
    print("5 is greater than 0")

if (my_bool):
    print("my_bool is true!")

if (my_bool):
    new_bool = False
    print("This new_bool is a local variable, it cannot be used outside of this block")



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
        



