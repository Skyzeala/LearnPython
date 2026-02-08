# Booleans are values that are either True or False, and can evaluate as 1 and 0 respectively if desired

my_bool = False
my_int = 0

print(my_bool)
print(str(type(my_bool)))

print(my_bool == 0)
print(True == 1)


# Code can be aggregated into what are called blocks
# In Python, blocks are defined by indentation, which is typically a tab or 4 spaces
# VSCode, and many other IDEs will automatically convert tabs to 4 spaces, to provide consistency
# You can learn more about typical Python coding style here
#     https://peps.python.org/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds

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
        



