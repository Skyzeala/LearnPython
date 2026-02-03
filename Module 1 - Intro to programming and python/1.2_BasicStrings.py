# Here are some things we can do with strings
# We use a lot of print statements here to show the outputs, 
# but the print statements are not the intended focus of this tutorial



# Here we combine two strings, note that '"' and "'" both work to define a string.
print('This is a string, and ' + "this is also a string.") #concatenate 2 strings using + operator
print("Concatenation is implicit" " for string literals") #concatenate 2 strings implicitly
print() #prints an empty line, helps to keep things formatted

print("Here we combine data types by converting an integer to a string: " + str(5))
# The concatenation operator (+ for strings) can only handle similar data types, we convert using str()
print("You can however, multiply " + "strings" * 3)
print()

# Miscellaneous ways of outputting strings
print("When printing long sequences, "
      "we can spread our code across multiple lines "
      "while keeping the string in tact") 

# These are called escaped characters, the escape symbol is a \ 
# and will attempt to escape the character following it
print("We can specify newlines in the middle of a string with \nbackslash n ")
print("We\tcan\talso\ttab with backslash t")
print("We can print backslashes by escaping the backslash with a backslash \\")
print(r"Sometimes we don't want to escape our \characters, so we can use a raw string instead")
print(r"Raw strings are useful for paths like D:\Downloads\code"
      "\nwhere the alternative can look messy D:\\Downloads\\code")
print()

#using quotations and special symbols
print("There are a few ways to use quote symbols")
print("You can specify them explicity by escaping them \" \' ")
print("Or use them freely so long as your 'current string' is not defined by them")

print('''
                This is a multi-line string literal, single 'quotes' don't need to be escaped
            It will output   almost   exactly what is between the 3 consecutive quotes
      If you want to ignore a newline, \
you can escape it
This is useful for easy formatting of larger blocks of text
      ''')

# Instead of string literals, we can use variables to store strings 
myString = "my string" #assignment operator
print(myString)

# Strings are a list of characters, and can be accessed per character basis
print("String type: " + str(type(myString)))

# Python uses zero indexing, which means a is at index 0, b is at index 1, c is at index 2, and so on
# The last character of a string will be at the index numbered one less than the length of the string
myString = "abcdef"
print("The length of myString is " + str(len(myString))) 
print(myString[0]) #prints the first character of a string
print(myString[3]) #print the character at index 4
print(myString[-1]) #print the character at the last index 
print(myString[-2]) #print the second last character
# Try changing the string and see how the outputs change
print("Note that these characters are still of type " + str(type(myString[0]))) 
# Other languages use 'char' as the type for individual characters
print()

myString = "abcdef"
print("Substrings")
print(myString[0:3]) #prints a substring from the first char and up to but not including the 4th char
print(myString[1:]) #print the substring starting at index 1, and going to the end of the string
print(myString[0:-1]) #print everything but the last character of a string

# Modification
# Strings in python are immutable, meaning they cannot be changed after creation
# To get around this, a new string must be made
myString = "thete is a typo in this statement"
print(myString)
myString = myString[:3] + 'r' + myString[4:]
print(myString)
# Writing something like 'myString[3] = r' would not work, as we cannot modify an existing string
# What happens on the backend is a new string gets made, and replaces the string stored in the variable
# Eventually, Pythons garbage collection system will come around and delete the old string from memory

# Each string variable is unique, and changing one will not change another
myString = "my string"
myNewString = myString

print(myNewString)
myString = "changed string"
print(myNewString)
print(myString)



