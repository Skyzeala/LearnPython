# Python is good at math, and many math operations are straightforward

print("Here are some basic math operations")
# The print function can also accept numbers as arguments
print(5+2) # addition
print(5-2) # subtraction
print(5*2) # multiplication
print(5/2) # division
print()

# Order of operations in Python is the same as algebra, and parentheses can be used to group numbers and prioritize
print("Order of operations in action: " + str(5+2*5))
print("Now with parentheses: " + str(2+(5+2)*2-2*3))
print()

print("Here are some other math operations")
print(5**2) # 5 to the power of 2
print(5//2) # 5 divided by 2, but the quotient is the number we keep and the remainder gets thrown away
print(5%2)  # 5 divided by 2, but the remainder is the number we keep and we toss away the quotient
print()

# With variables, we can edit them in place, this can save space when editing an existing variable
print("Here we do some math in place on some variables")
x = 5
# If we wanted to add 2 to this x variable, one way would be like this
x = x + 2
print ("x = x + 2, x = " + str(x))
# but the preferred method is incrementing in place
x += 2 # Add 2 to x, then assign x the value of the result
print("x += 2, x = " + str(x))
# In place operations work will all basic math operation
x = 5
x -= 2 
print(x)
x = 5
x *= 2 
print(x)
x = 5
x /= 2 
print(x)
x = 5
x **= 2 
print(x)
x = 5
x //= 2 
print(x)
x = 5
x %= 2 
print(x)

# There are also a lot of built-in math functions that don't require libraries
print(abs(-3)) # absolute value
print(pow(5, 2)) # exponent, equivalent to 5 ** 2
print(min(10, 20, 1, 12, 31)) # find the minimum value of 2 or more numbers
print(max(1, 20, 4, 56)) # find the maximum value of 2 or more numbers


# Numbers and data types
print("We have used " + str(type(5)) + " typed values so far, but")
print("We can also use " + str(type(5.1)) + " numbers " + str(5.1+2.1)) 
# Floats, or floating point numbers can be specified by including a decimal point in the number
# Note the result, decimal values are always approximated due to computer hardware limitations

# Ints, floats, and other number types can be intermixed, 
#     and will always give a result of the most precise one used
print("For example, 5 + 5.0 = " + str(5+5.0))
print("To convert a float to an int, use the int() function to round down " + str(int(5.6)))
print("Or the round function can be used for normal rounding " + str(round(5.6)))
print()

# The round function has a second argument (which defaults to 0 when unused)
#     to signify how many decimal places to round to, where negative values round to incrementally larger places
print(round(456.789, 2)) # round to the hundredths place, 2 decimal places
print(round(456.789, 1)) # round to the tenths place, 1 decimal place
print(round(456.789)) # round to the zeroth place, no decimal places, the trailing .0 shows that it is still a float
print(round(456.789, -1)) # round to nearest tens place
print(round(456.789, -2)) # round to nearest hundreds place
# Rounding can also be done with ints
