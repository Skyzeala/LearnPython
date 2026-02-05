# Python is good at math, note that it DOES use order of operations



print("Here are some basic math operations")
print(5+2) # addition
print(5-2) # subtraction
print(5*2) # multiplication
print(5/2) # division
print("Order of operations in action " + str(5+2*5))
print("Now with parentheses " + str(2+(5+2)*2-2*3))
print()

print("Here are some other math operations")
print(5**2) # 5 to the power of 2
print(5//2) # 5 divided by 2, but the remainder gets thrown away
print(5%2)  # 5 divided by 2, but the remainder is the number we keep
print()

# With variables, we can edit them in place
print("Here we do some math in place on some variables")
x = 5
x += 2 
print(x)
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

# Numbers and data types
print("We have used " + str(type(5)) + " typed values so far, but")
print("these also work for " + str(type(5.1)) + " numbers " + str(5.1+2.1)) 
# note the result, decimal values are always approximated due to computer hardware limitations

# Ints and floats can be intermixed, and will always give a result of the most precise one used
print("For example, 5 + 5.0 = " + str(5+5.0))
print("To convert back to an int, use the int() function to round down " + str(int(5.6)))
print("Or the round function can be used " + str(round(5.6)))
print()



# Python data types are dynamic, they are determined at runtime and not explicitly stated in the code



#two variables can be defined at once

var1, var2 = 1, 2
print(str(var1) + " " + str(var2))



#rand


